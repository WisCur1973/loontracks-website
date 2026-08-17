#!/bin/bash
# blog-publish.sh - publish new/updated blog posts to the live site.
#
# Write a post in content/posts/<slug>/index.md (with its images in that same
# folder), then run this script. Safe to run from ANY Mac that has this repo
# cloned: it locates the repo relative to itself (no hardcoded username/path),
# pulls first so it stays in sync with the desktop's automated model pushes,
# then pushes. The remote build (Cloudflare) redeploys automatically.
#
# Usage:
#   ./blog-publish.sh                 # auto commit message
#   ./blog-publish.sh "My message"    # custom commit message
set -euo pipefail

# Locate the repo = the directory this script lives in.
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO"

MSG="${1:-Blog: update $(date '+%Y-%m-%d %H:%M')}"

# Only the blog lives here; model dashboards are published separately by
# sync-models.sh. Stage posts (text + their bundled images).
git add content/posts

if git diff --cached --quiet; then
    echo "Nothing to publish (no staged changes in content/posts)."
    exit 0
fi

echo "Committing: $MSG"
git commit -m "$MSG"

# Pull first (rebase our post on top of anything the desktop automation pushed)
# so the push fast-forwards cleanly. --autostash protects any other in-progress
# edits. A genuine conflict stops here for you to resolve.
echo "Syncing with GitHub (pull --rebase)..."
git pull --rebase --autostash origin main

echo "Pushing..."
git push origin main
echo "Published. The site will rebuild and redeploy automatically."
