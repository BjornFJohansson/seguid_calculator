#!/usr/bin/env bash
source appveyor_source_file.sh
conda config --set always_yes yes --set show_channel_urls yes
conda update --yes -q conda
conda config --prepend channels conda-forge 
conda config --append channels BjornFJohansson
conda create -yq -n seguidcondabuild36 python=3.6 wxpython pyinstaller
source activate seguidcondabuild36
python setup.py build
cat build/lib/seguid_calculator/_version.py
pyinstaller --onefile seguid_calculator.py
ls dist/
wc -c dist/seguid_calculator.exe
appveyor PushArtifact dist/seguid_calculator.exe
