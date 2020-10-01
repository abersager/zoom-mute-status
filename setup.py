from setuptools import setup

OPTIONS = {
    'argv_emulation': True,
    'iconfile':'assets/app_icon.icns',
    'plist': {
        'LSUIElement': True,
        'CFBundleShortVersionString':'0.1.0',
    },
    'packages': ['rumps'],
}

setup(
    app=['zoom-mute-status.py'],
    name="Zoom Mute Status",
    data_files=[
        ('assets', ['assets/muted.png', 'assets/unmuted.png'])
    ],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
