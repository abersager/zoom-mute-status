# Zoom Mute Status for macOS

Quick and dirty menu bar app to display current Zoom Mute / Unmute status. This is a workaround for a missing feature in the zoom.us macOS app.

Zoom has the ability to define global shortcuts, and I make heavy use of global mute / unmute, staying on mute during calls and working in other apps until I've got something to say. However, the Zoom window may be obscured by other windows, and then there's no way to tell if you're currently muted or not. Although Zoom can display an icon in the right "status menus" section of the menu bar, the icon doesn't tell you whether you're currently muted or not.

Zoom Mute Status adds another icon to the status menus section, which indicates current mute status. This is achieved by polling the current mute status of Zoom via AppleScript every second, which of course is less than ideal. Once Zoom's own menu bar can display this information, this app is obsolete.


## Build

```
./install-dependencies.sh
./build.sh
mv dist/Zoom\ Mute\ Status.app /Applications/
```

## Acknowledgements

Built using [rumps](https://github.com/jaredks/rumps).

Icons courtesy of Ziyad Al junaidi via Noun Project:
- https://thenounproject.com/search/?q=microphone&i=3530293
- https://thenounproject.com/search/?q=microphone&i=3530319
