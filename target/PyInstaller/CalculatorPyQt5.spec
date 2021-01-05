# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\Programing\\Learn\\pyQtCalc\\src\\main\\python\\main.py'],
             pathex=['D:\\Programing\\Learn\\pyQtCalc\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['D:\\Programing\\Learn\\pyQtCalc\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='CalculatorPyQt5',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='D:\\Programing\\Learn\\pyQtCalc\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='CalculatorPyQt5')
