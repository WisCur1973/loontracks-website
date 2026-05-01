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

# Sync Respiratory Dashboard
echo "🫁 Syncing respiratory dashboard..."
cp "/Users/danielwinings/Library/CloudStorage/ProtonDrive-daniel@loontracks.com-folder/respiratory_dashboard.html" \
   "static/static-dashboards/respiratory_dashboard.html"
echo "   - static/static-dashboards/respiratory_dashboard.html"

echo "🗳️  Syncing election forecasts..."
cp "/Users/danielwinings/Library/CloudStorage/ProtonDrive-daniel@loontracks.com-folder/Elections/State Legislature Forecast/output/"*.html "static/elections/"

# Verify both dated and latest versions exist
echo "🔍 Verifying election forecast files..."
latest_files=("Congressional_Forecast_latest.html" "Governor_Forecast_latest.html" "MI_Legislature_Forecast_latest.html" "MN_Legislature_Forecast_latest.html" "WI_Legislature_Forecast_latest.html")
for file in "${latest_files[@]}"; do
    if [ -f "static/elections/$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ $file (missing)"
    fi
done

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
