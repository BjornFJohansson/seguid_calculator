#!/usr/bin/env bash
source appveyor_source_file.sh
conda config --set always_yes yes --set show_channel_urls yes
conda update --yes -q conda
conda config --prepend channels conda-forge 
conda config --append channels BjornFJohansson
conda create -yq -n seguidcondabuild36 python=3.6
source activate seguidcondabuild36
conda install wxpython
conda install pyinstaller
brew install upx
conda install pypandoc
python setup.py build
cat build/lib/seguid_calculator/_version.py
pyinstaller --onefile --windowed seguid_calculator/seguid.py
ls dist/
wc -c dist/seguid.exe
