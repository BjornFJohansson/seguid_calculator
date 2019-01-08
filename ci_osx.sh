#!/usr/bin/env bash
wget -q http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O Miniconda_latest.sh
bash Miniconda_latest.sh
conda config --set always_yes yes --set show_channel_urls yes
conda update --yes -q conda
conda config --prepend channels conda-forge 
conda config --append channels BjornFJohansson
conda create -yq -n seguidcondabuild36 python=3.6 wxpython pyinstaller
source activate seguidcondabuild36
pyinstaller --onefile --windowed --icon=calc.ico seguid_calculator.py
wc -c dist/seguid_calculator.app
