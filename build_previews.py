#!/usr/bin/env python3
"""
build_previews.py - generate homepage carousel preview images.

Writes PNGs into static/previews/ for the center-column carousel on the Loon
Tracks homepage. Run AFTER the model HTML has been synced into static/ (it is
invoked from sync-models.sh, so previews always reflect the freshly published
dashboards).

Two mechanisms, because the source pages render very differently:

  * Congressional (WI map) - extracted straight from the base64 PNG that the
    matplotlib map is embedded as inside Congressional_Forecast_latest.html.
    No browser needed; highest fidelity.

  * Governor, MI/MN/WI legislatures, iron port - rendered with headless
    Chromium (Playwright) and cropped to a "hero" region, because those pages
    draw with Chart.js (canvas), HTML tables, and inline SVG respectively and
    contain no static image to lift out.

Each preview is paired with a caption + link in content/_index.md.
"""

import base64
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
OUT = STATIC / "previews"
SCALE = 2  # device_scale_factor for crisp Retina previews


def log(msg):
    print(f"  {msg}", flush=True)


# --------------------------------------------------------------------------- #
# 1. Congressional WI map - base64 extraction (no browser)                    #
# --------------------------------------------------------------------------- #
def png_dims(raw):
    if raw[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", raw[16:24])
        return w, h
    return None


# The three state maps are ~700x790 portrait matplotlib PNGs; identify by size.
MAP_DIMS = {
    (665, 790): "congressional_mi.png",
    (697, 790): "congressional_mn.png",
    (721, 790): "congressional_wi.png",
}


def extract_maps():
    src = STATIC / "elections" / "Congressional_Forecast_latest.html"
    if not src.exists():
        log(f"SKIP congressional maps: {src.name} missing")
        return
    html = src.read_text(encoding="utf-8", errors="ignore")
    found = set()
    for _, data in re.findall(r"data:image/(png|jpeg);base64,([A-Za-z0-9+/=]+)", html):
        raw = base64.b64decode(data)
        name = MAP_DIMS.get(png_dims(raw))
        if name and name not in found:
            (OUT / name).write_bytes(raw)
            found.add(name)
            w, h = png_dims(raw)
            log(f"{name}  ({len(raw)//1024} KB, {w}x{h})")
    for dims, name in MAP_DIMS.items():
        if name not in found:
            log(f"WARN {name}: {dims[0]}x{dims[1]} PNG not found in dashboard")


# --------------------------------------------------------------------------- #
# 2. Screenshot jobs - Chromium via Playwright                                #
# --------------------------------------------------------------------------- #
# clip = union bounding box of every element matching any `clip` selector,
# grown by `pad` px (and `top_extra` px above, to catch a heading).
# `hide` selectors are set display:none before measuring, so detailed tables
# don't bloat the crop.
SHOTS = [
    {
        "name": "governor.png",
        "file": "elections/Governor_Forecast_latest.html",
        "width": 1440,
        "clip": [".state-cards", ".trend-section"],
        "hide": [],
        "pad": 24,
        "top_extra": 0,
    },
    {
        "name": "mi_legislature.png",
        "file": "elections/MI_Legislature_Forecast_latest.html",
        "width": 1240,
        "clip": [".header", ".summary-bar", ".rating-bar"],
        "hide": ["table", ".county-table-scroll"],
        "pad": 20,
        "top_extra": 0,
    },
    {
        "name": "mn_legislature.png",
        "file": "elections/MN_Legislature_Forecast_latest.html",
        "width": 1240,
        "clip": [".header", ".summary-bar", ".rating-bar"],
        "hide": ["table", ".county-table-scroll"],
        "pad": 20,
        "top_extra": 0,
    },
    {
        "name": "wi_legislature.png",
        "file": "elections/WI_Legislature_Forecast_latest.html",
        "width": 1240,
        "clip": [".header", ".summary-bar", ".rating-bar"],
        "hide": ["table", ".county-table-scroll"],
        "pad": 20,
        "top_extra": 0,
    },
    {
        "name": "iron_port.png",
        "file": "models/port_forecasts_dashboard.html",
        "width": 1100,
        "clip": [".header", ".gauges-grid"],
        "hide": [],
        "pad": 24,
        "top_extra": 0,
    },
]

UNION_JS = """
(args) => {
  const [clipSel, hideSel] = args;
  hideSel.forEach(s => document.querySelectorAll(s).forEach(el => el.style.display = 'none'));
  let x1 = Infinity, y1 = Infinity, x2 = -Infinity, y2 = -Infinity, n = 0;
  clipSel.forEach(s => document.querySelectorAll(s).forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    x1 = Math.min(x1, r.left); y1 = Math.min(y1, r.top);
    x2 = Math.max(x2, r.right); y2 = Math.max(y2, r.bottom); n++;
  }));
  if (!n) return null;
  return {x: x1, y: y1, w: x2 - x1, h: y2 - y1,
          pw: document.documentElement.scrollWidth,
          ph: document.documentElement.scrollHeight};
}
"""


def run_shots():
    from playwright.sync_api import sync_playwright

    ok = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for job in SHOTS:
            src = STATIC / job["file"]
            if not src.exists():
                log(f"SKIP {job['name']}: {job['file']} missing")
                continue
            page = browser.new_page(
                viewport={"width": job["width"], "height": 1200},
                device_scale_factor=SCALE,
            )
            try:
                page.goto(src.as_uri(), wait_until="networkidle", timeout=30000)
            except Exception:
                # networkidle can hang on CDN keep-alives; DOM + a pause is enough
                page.wait_for_timeout(1500)
            page.wait_for_timeout(1800)  # let Chart.js finish animating / fonts settle

            box = page.evaluate(UNION_JS, [job["clip"], job["hide"]])
            if not box:
                log(f"WARN {job['name']}: no clip elements matched; full page")
                page.screenshot(path=str(OUT / job["name"]), full_page=True)
            else:
                pad, top = job["pad"], job["top_extra"]
                x = max(0, box["x"] - pad)
                y = max(0, box["y"] - pad - top)
                w = min(box["pw"] - x, box["w"] + 2 * pad)
                h = min(box["ph"] - y, box["h"] + 2 * pad + top)
                page.screenshot(
                    path=str(OUT / job["name"]),
                    clip={"x": x, "y": y, "width": w, "height": h},
                )
                log(f"{job['name']}  ({int(w)}x{int(h)} @{SCALE}x)")
            ok += 1
            page.close()
        browser.close()
    return ok


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print("Building homepage carousel previews...", flush=True)
    extract_maps()
    try:
        run_shots()
    except Exception as e:  # never let a preview failure break the publish
        print(f"  WARN screenshot step failed: {e}", file=sys.stderr, flush=True)
    print("Done.", flush=True)


if __name__ == "__main__":
    main()
