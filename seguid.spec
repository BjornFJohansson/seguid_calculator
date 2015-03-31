# -*- mode: python -*-
a = Analysis(['./seguid_calculator/seguid.py'],
             pathex=['/home/bjorn/python_packages/seguid_calculator'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='seguid',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='calc.ico')
