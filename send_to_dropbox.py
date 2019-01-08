#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import dropbox

try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib

   
def upload(pth, parent=pathlib.Path("/Public")):
    np = parent.joinpath(pth)
    print("uploading", pth, "to", np)
    with pth.open('rb') as f:
        try:
            dbx.files_upload(f.read(), str(np), mode=dropbox.files.WriteMode('overwrite'))
        except dropbox.exceptions.ApiError as err:
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

dbx = dropbox.Dropbox( os.environ["DROPBOXTOKEN"] )

try:
    dbx.users_get_current_account()
except dropbox.exceptions.AuthError as err:
    sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

npths = (pathlib.Path(p) for p in ( "seguid_calculator_for_mac.zip" ))
    
for pth in npths:
    try: 
        upload(pth, pathlib.Path("/Public/hej"))
    except FileNotFoundError:
        print(pth, "not found.")
