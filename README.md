# Loon Tracks Website

Professional market intelligence and forecasting website built with Hugo static site generator.

## 🏗️ Site Structure

### Content Sections
- **Blog** (`/blog/`) - Market analysis and written content (3x/week)
- **Forecasts** (`/forecasts/`) - Weekly probability models and dashboards
- **About** (`/about/`) - Methodology and background information

### Features
- Responsive design optimized for all devices
- Built-in newsletter signup (Netlify Forms)
- Search and archive functionality
- Dashboard integration ready
- SEO optimized
- Professional market intelligence branding

## 🚀 Quick Start

### Prerequisites
1. Install Hugo: https://gohugo.io/getting-started/installing/
2. Clone/download this website folder

### Local Development
```bash
cd website
hugo server -D
```
Visit: http://localhost:1313

### Build for Production
```bash
hugo
```
Output in `public/` folder

## 📝 Content Management

### Adding Blog Posts
```bash
hugo new blog/YYYY-MM-DD-post-title.md
```

### Adding Forecasts
```bash
hugo new forecasts/YYYY-MM-DD-forecast-title.md
```

### Content Templates
- Blog posts: Standard markdown with categories/tags
- Forecasts: Include `dashboard_image` and `data_sources` frontmatter

## 🎨 Theme Structure

```
themes/loontracks-theme/
├── layouts/
│   ├── _default/
│   │   ├── baseof.html      # Base template
│   │   ├── list.html        # Blog/forecast listings
│   │   └── single.html      # Individual posts
│   ├── partials/
│   │   ├── header.html      # Site header/navigation
│   │   └── footer.html      # Footer with newsletter signup
│   └── index.html           # Homepage
└── static/
    ├── css/style.css        # Main stylesheet
    └── js/main.js           # JavaScript functionality
```

## 📊 Dashboard Integration

The site is ready for your forecast dashboard integration:

1. **Dashboard Images**: Place PNG files in `static/forecasts/images/`
2. **HTML Dashboards**: Add `dashboard_html` frontmatter to forecast posts
3. **Automatic Publishing**: Ready for your one-click publishing system

### Sample Forecast Frontmatter
```yaml
---
title: "Weekly Mine Forecast"
date: 2026-02-19
forecast_type: "Mine Operations"
dashboard_image: "/forecasts/images/unified_mine_forecast_dashboard.png"
data_sources:
  - "AISI Great Lakes Steel Production Data"
  - "Port Physical Stockpile Observations"
---
```

## 🌐 Deployment Options

### Option 1: Netlify (Recommended)
1. Connect your Git repository to Netlify
2. Build command: `hugo`
3. Publish directory: `public`
4. Domain: Connect your www.loontracks.com domain

### Option 2: GitHub Pages
1. Push to GitHub repository
2. Use GitHub Actions for Hugo build
3. Deploy to `gh-pages` branch

### Option 3: Traditional Hosting
1. Run `hugo` to build
2. Upload `public/` folder contents to web hosting
3. Point domain to hosting directory

## 📧 Newsletter Integration

Currently configured for:
- **Netlify Forms** for email capture
- **Substack integration** links
- Ready for migration to paid newsletter service

### Newsletter Form
The footer includes a newsletter signup form that:
- Captures emails via Netlify Forms
- Links to your current Substack
- Prepared for future premium newsletter migration

## 🔧 Configuration

### Site Settings
Edit `config.yaml` to customize:
- Site title and description
- Menu structure
- Newsletter settings
- Analytics (when ready)

### Theme Customization
- **CSS**: Modify `static/css/style.css`
- **JavaScript**: Extend `static/js/main.js`
- **Templates**: Customize layouts in `themes/loontracks-theme/layouts/`

## 📱 Mobile Optimization

The site is fully responsive with:
- Mobile-first design approach
- Touch-friendly navigation
- Optimized dashboard viewing on mobile devices
- Fast loading on all connection types

## 🔍 SEO Features

Built-in SEO optimization:
- Meta tags and Open Graph integration
- Structured data for articles and forecasts
- XML sitemap generation
- Clean, semantic URLs

## 📈 Analytics Ready

Prepared for analytics integration:
- Google Analytics configuration ready
- Privacy-compliant tracking setup
- Conversion tracking for newsletter signups

## 🛠️ Next Steps

1. **Test locally**: Run `hugo server` and review the site
2. **Add your logo**: Replace placeholder logo files
3. **Customize content**: Update About page and sample posts
4. **Connect domain**: Set up hosting and domain connection
5. **Dashboard integration**: Connect your forecast publishing system

---

*Ready for your market intelligence publishing platform! 🚀*