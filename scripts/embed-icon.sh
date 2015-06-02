#!/bin/bash

#1) navigate to the WX tool directory, on my installation that's 
#   C:\Python24\Lib\site-packages\wx-2.8-msw-unicode\wx\tools 

#2) run "img2py.py -i pycon.ico iconfile.py" 

#3) copy the iconfile.py to your project's directory 

#4) put these lines in your app: 

# import iconfile 
# myicon = iconfile.getIcon() 
# self.SetIcon(myicon) 


python /usr/local/lib/python2.7/dist-packages/wx/tools/img2py.py -i calc.ico calc_icon_file.py
