#!/bin/bash
# Deploy script for traditional web hosting

echo "Building Hugo site..."
hugo --minify --cleanDestinationDir

echo "Site built in public/ directory"
echo "Upload the contents of public/ directory to your web hosting"
echo ""
echo "Via FTP/SFTP upload these files:"
echo "- All contents of public/ folder"
echo "- Upload to your domain's document root (usually public_html/ or www/)"
echo ""
echo "Or zip the public folder contents and extract on your server"

# Optional: Create zip file for upload
if command -v zip &> /dev/null; then
    echo "Creating zip file for easy upload..."
    cd public
    zip -r ../loontracks-website.zip .
    cd ..
    echo "Created loontracks-website.zip - upload and extract this on your server"
fi