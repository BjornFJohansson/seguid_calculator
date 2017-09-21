#!/usr/bin/env bash
wget http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh --quiet
bash ~/miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
conda update --yes -q conda
#conda create -yq -n pydnacondabuild35 python=3.5
#source activate pydnacondabuild35
conda install -c conda-forge wxpython=4.0.0a3
pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
brew install upx
#conda install --yes -c conda-forge pyinstaller
conda install -c conda-forge pypandoc
python setup.py build
cat build/lib/seguid_calculator/_version.py
pyinstaller --onefile --windowed seguid_calculator.spec
cat build/seguid_calculator/warnseguid_calculator.txt
hdiutil create dist/seguid_calculator.dmg -srcfolder dist/ -ov
zip -r dist/seguid_calculator.zip dist/seguid_calculator.app
ls dist/
wc -c dist/seguid_calculator.zip
wc -c dist/seguid_calculator.dmg
pip install -I dropbox==6.9.0
python deploy_to_dropbox.py
