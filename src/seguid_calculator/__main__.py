#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring."""

from flaskwebgui import FlaskUI

from seguid_calculator.app import app

FlaskUI(app=app, server="flask").run()
