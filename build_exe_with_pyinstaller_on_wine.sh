#!/bin/bash

wine C:/Python27/python.exe pyinstaller/pyinstaller.py --noconsole --icon=calc.ico --onefile SEGUID_calculator_current.py

read -p "Press [Enter] key..."
