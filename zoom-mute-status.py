import rumps
import subprocess
import sys
import os

base_path = os.path.dirname(os.path.abspath(__file__))

icon_muted = base_path + "/assets/muted.png"
icon_unmuted = base_path + "/assets/unmuted.png"

script = '''property btnTitle : "Mute audio"

tell application "System Events" to tell application process "zoom.us"
	if exists (menu item btnTitle of menu 1 of menu bar item "Meeting" of menu bar 1) then
		do shell script "echo unmuted"
	else
		do shell script "echo muted"
	end if
end tell
'''

class ZoomMuteStatusBarApp(rumps.App):
  @rumps.timer(1)
  def loop(self, _):
    proc = subprocess.Popen(['osascript', '-'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE)
    output = proc.communicate(script)[0].strip()

    if output == "muted":
      self.icon = icon_muted
    else:
      self.icon = icon_unmuted


if __name__ == "__main__":
  ZoomMuteStatusBarApp("Zoom Mute Status", icon=icon_muted).run()
