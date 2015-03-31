#!/bin/bash

pyinstaller --noconsole --icon=calc.ico --onefile ./seguid_calculator/seguid.py

read -p "Press [Enter] key..."
