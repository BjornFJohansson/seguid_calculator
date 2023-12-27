#!/usr/bin/env bash

# pyinstaller --onefile --disable-windowed-traceback --windowed --icon=calc.ico --name seguid_calculator src/gui.py

pyinstaller --copy-metadata seguid_calculator2 --onefile --disable-windowed-traceback --windowed --icon=calc.ico --name seguid_calculator2 src/seguid_calculator2/calculator.py
