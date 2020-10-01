from setuptools import setup

OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=['zoom-mute-status.py'],
    name="Zoom Mute Status",
    data_files=[],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
