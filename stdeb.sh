#!/usr/bin/env bash


find . -name \*.pyc -delete


python setup.py --command-packages=stdeb.command bdist_deb


echo "press any key to close"
read -n1 slask
