#!/usr/bin/env bash
rm -rf dmg
mkdir -p dmg
create-dmg "dmg/zoom-mute-status.dmg" "dist/"
