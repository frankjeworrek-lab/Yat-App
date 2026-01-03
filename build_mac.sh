#!/bin/bash
set -e

echo "🏗️  Building Y.A.T. macOS App..."

# Ensure pyinstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "📦 Installing PyInstaller..."
    pip install pyinstaller
fi

# 1. Prepare Icon
echo "🎨 Generating .icns from logo/dock.png with Pillow..."
rm -rf build/icon.iconset
# Use python script for high-quality resize with transparency preservation and zoom (crop checkers)
python3 tools/icon_gen.py logo/dock.png build/icon.iconset 1.6

iconutil -c icns build/icon.iconset -o build/YAT.icns

# 2. Build App
echo "🔨 Running PyInstaller..."
# Note: We use --collect-all nicegui to ensure all templates are included
# We manually add data folders.

pyinstaller main.py \
    --name "YAT" \
    --windowed \
    --icon "build/YAT.icns" \
    --add-data "logo:logo" \
    --add-data "ui_nicegui:ui_nicegui" \
    --add-data "core:core" \
    --add-data "plugins:plugins" \
    --add-data "storage:storage" \
    --add-data "docs:docs" \
    --collect-all nicegui \
    --collect-all webview \
    --collect-all openai \
    --collect-all google \
    --collect-all anthropic \
    --clean \
    --noconfirm

# Rename correctly
rm -rf "dist/Y.A.T.app"
mv "dist/YAT.app" "dist/Y.A.T.app"

echo "✨ Build Complete!"
echo "👉 You can now drag 'dist/Y.A.T.app' to your Applications folder or Dock."
