# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['cochavim_uzmanim_plus.py'],
    pathex=[],
    binaries=[],
    datas=[('cu_icon.ico', '.'), ('hyi_icon.ico', '.'), ('converter_icon.ico', '.'), ('birthday_icon.ico', '.'), ('cochavim_uzmanim_plus.py', '.'), ('cochavim_uzmanim_plus_dir.exe', '.'), ('cu_locations.csv', '.'), ('cu_stars.csv', '.'), ('cu_splash.jpg', '.'), ('de440.bsp', '.'), ('skyfield', 'skyfield'),],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
splash = Splash(
    'cu_splash.jpg',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=(10, 50),
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='cochavim_uzmanim_plus',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['cu_icon.ico'],
)
