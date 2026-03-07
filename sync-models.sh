#!/bin/bash
# sync-models.sh - Sync model HTML files to Hugo after each model run

echo "🔄 Syncing model files to Hugo website..."

# Create directories if they don't exist
mkdir -p static/models
mkdir -p static/elections

# Sync MN Iron Industry (Taconite) Dashboards
echo "📊 Syncing taconite dashboards..."
cp "/Users/danielwinings/Library/CloudStorage/ProtonDrive-daniel@loontracks.com-folder/claude taconite hybrid prototype/unified_mine_forecast_dashboard.html" "static/models/"
cp "/Users/danielwinings/Library/CloudStorage/ProtonDrive-daniel@loontracks.com-folder/claude taconite hybrid prototype/port_forecasts_dashboard.html" "static/models/"

# Sync Election Forecasts

# Sync Measles Dashboard
echo "🦠 Syncing measles dashboard..."
mkdir -p static/static-dashboards
cp "/Users/danielwinings/Library/CloudStorage/ProtonDrive-daniel@loontracks.com-folder/MMR mapping files/measles_dashboard_multistate.html" \
   "static/static-dashboards/measles_dashboard_multistate.html"
echo "   - static/static-dashboards/measles_dashboard_multistate.html"

# Sync Respiratory Dashboard
echo "🫁 Syncing respiratory dashboard..."
cp "/Users/danielwinings/Library/CloudStorage/ProtonDrive-daniel@loontracks.com-folder/respiratory_dashboard.html" \
   "static/static-dashboards/respiratory_dashboard.html"
echo "   - static/static-dashboards/respiratory_dashboard.html"

echo "🗳️  Syncing election forecasts..."
cp "/Users/danielwinings/Library/CloudStorage/ProtonDrive-daniel@loontracks.com-folder/Election Probabilities/"*.html "static/elections/"

echo "✅ All model files synced successfully!"
echo "📁 Files copied to:"
echo "   - static/models/unified_mine_forecast_dashboard.html"
echo "   - static/models/port_forecasts_dashboard.html"
echo "   - static/elections/*.html ($(ls static/elections/*.html | wc -l) files)"
echo ""

# Auto-commit and push to GitHub
echo "🔄 Auto-committing and pushing to GitHub..."
git add static/models/ static/elections/ static/static-dashboards/
git commit -m "Auto-update: Model forecasts $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
echo "✅ Changes pushed to GitHub!"
