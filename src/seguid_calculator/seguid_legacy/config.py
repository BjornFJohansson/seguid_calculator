#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import warnings
from .manip import min_rotation_py

## The min_rotation() function
_min_rotation=min_rotation_py

def set_min_rotation(which):
    assert isinstance(which, str), "Argument 'which' must be an string"
    if which == "built-in":
        _min_rotation=min_rotation_py
    elif which == "pydivsufsort":
        from pydivsufsort import min_rotation as mr
        def min_rotation_pydivsufsort(s):
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
            result = mr(s)
            return result
        _min_rotation=min_rotation_pydivsufsort
    else:
        raise ValueError("Argument 'which' should be either 'built-in' or '': " + which)
