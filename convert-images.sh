#!/usr/bin/env bash
cd assets
rsvg-convert muted.svg > muted.png
rsvg-convert unmuted.svg > unmuted.png

mkdir -p app_icon.iconset
rsvg-convert -h 16 unmuted.svg > app_icon.iconset/icon_16x16.png
rsvg-convert -h 32 unmuted.svg > app_icon.iconset/icon_16x16@2x.png
cp app_icon.iconset/icon_16x16@2x.png app_icon.iconset/icon_32x32.png
rsvg-convert -h 64 unmuted.svg > app_icon.iconset/icon_32x32@2x.png
rsvg-convert -h 128 unmuted.svg > app_icon.iconset/icon_128x128.png
rsvg-convert -h 256 unmuted.svg > app_icon.iconset/icon_128x128@2x.png
cp app_icon.iconset/icon_128x128@2x.png app_icon.iconset/icon_256x256.png
rsvg-convert -h 512 unmuted.svg > app_icon.iconset/icon_256x256@2x.png
cp app_icon.iconset/icon_256x256@2x.png app_icon.iconset/icon_512x512.png
rsvg-convert -h 1024 unmuted.svg > app_icon.iconset/icon_512x512@2x.png

iconutil --convert icns app_icon.iconset
rm -rf app_icon.iconset
