# -*- mode: python -*-

block_cipher = None


a = Analysis(['build/lib/seguid_calculator/seguid.py'],
             pathex=['/home/bjorn/python_packages/seguid_calculator/seguid_calculator'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='seguid_calculator',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='calc.ico')
