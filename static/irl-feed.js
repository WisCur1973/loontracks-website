/* irl-feed.js — pulls the latest IRL posts from Micro.blog and renders them.
 *
 * Runs entirely in the visitor's browser and reads wiscur.micro.blog/feed.json
 * (which sends Access-Control-Allow-Origin: *), so new posts show up on
 * loontracks with no rebuild. Populates #irl-latest (homepage panel, newest
 * post) and/or #irl-list (the IRL page, recent posts). If the feed can't be
 * reached, the fallback links already in those containers are left in place.
 */
(function () {
  var FEED = "https://wiscur.micro.blog/feed.json";
  var latestEl = document.getElementById("irl-latest");
  var listEl = document.getElementById("irl-list");
  if (!latestEl && !listEl) return;

  function parse(html) {
    return new DOMParser().parseFromString(html || "", "text/html");
  }
  function textFromHtml(html) {
    return (parse(html).body.textContent || "").replace(/\s+/g, " ").trim();
  }
  function imageFromHtml(html) {
    var doc = parse(html);
    var img = doc.querySelector("img");
    if (img && img.getAttribute("src")) return img.getAttribute("src");
    var vid = doc.querySelector("video[poster]");
    if (vid) return vid.getAttribute("poster");
    return "";
  }
  function truncate(s, n) {
    s = s || "";
    return s.length > n ? s.slice(0, n - 1).replace(/\s+\S*$/, "") + "…" : s;
  }
  function fmtDate(iso) {
    var d = new Date(iso);
    return isNaN(d) ? "" : d.toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" });
  }
  function esc(s) {
    return (s || "").replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function fields(item) {
    var text = textFromHtml(item.content_html);
    var hasTitle = !!(item.title || "").trim();
    return {
      url: item.url,
      title: hasTitle ? item.title.trim() : (truncate(text, 70) || "Untitled post"),
      date: fmtDate(item.date_published),
      excerpt: hasTitle ? truncate(text, 170) : truncate(text, 170),
      img: imageFromHtml(item.content_html)
    };
  }

  function card(item) {
    var f = fields(item);
    return '<a class="blog-card" href="' + esc(f.url) + '" target="_blank" rel="noopener">' +
      (f.img ? '<div class="blog-card-thumb" style="background-image:url(\'' + esc(f.img) + '\')"></div>' : "") +
      '<div class="blog-card-body">' +
        '<div class="blog-card-kicker">Math: IRL</div>' +
        '<div class="blog-card-title">' + esc(f.title) + '</div>' +
        (f.date ? '<div class="blog-card-date">' + esc(f.date) + '</div>' : "") +
        (f.excerpt ? '<div class="blog-card-summary">' + esc(f.excerpt) + '</div>' : "") +
      '</div>' +
    '</a>';
  }

  function row(item) {
    var f = fields(item);
    return '<a class="irl-row" href="' + esc(f.url) + '" target="_blank" rel="noopener">' +
      (f.img ? '<div class="irl-row-thumb" style="background-image:url(\'' + esc(f.img) + '\')"></div>' : "") +
      '<div class="irl-row-body">' +
        '<div class="irl-row-title">' + esc(f.title) + '</div>' +
        (f.date ? '<div class="irl-row-date">' + esc(f.date) + '</div>' : "") +
        (f.excerpt ? '<div class="irl-row-summary">' + esc(f.excerpt) + '</div>' : "") +
      '</div>' +
    '</a>';
  }

  fetch(FEED, { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (feed) {
      var items = feed.items || [];
      if (!items.length) return;
      if (latestEl) latestEl.innerHTML = card(items[0]);
      if (listEl) listEl.innerHTML = items.slice(0, 10).map(row).join("");
    })
    .catch(function () { /* leave the fallback links in place */ });
})();
