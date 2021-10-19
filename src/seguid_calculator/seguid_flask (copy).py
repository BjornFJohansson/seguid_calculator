#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring."""

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from wtforms.fields import SelectField
from wtforms.fields import DecimalField
from wtforms.fields import TextAreaField
from wtforms.fields import SubmitField

from .functions import seqfilter
from .functions import seguid
from .functions import rc
from .functions import cseguid
from .functions import lseguid

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful_secretkey",
    WTF_CSRF_SECRET_KEY="a_csrf_secret_key"))

results = []
results.append("1")
results.append("2")
results.append("3")
results.append("4")

@app.route("/", methods=["GET", "POST"])
def index():
    """docstring."""

    if request.method == "GET":
        return render_template("index.html",
                               results=results)

    if 'clear' in request.form:
        results.clear()
        return redirect(url_for('index'))
    
    print("---", request.form)
    sequence = seqfilter(request.form["sequence"])

    results[0] = seguid(sequence)
    results[1] = cseguid(sequence)
    results[2] = lseguid(sequence)
    results[3] = sequence

    return redirect(url_for('index'))

if __name__ == '__main__':
    from webui import WebUI
    ui = WebUI(app, debug=True)
    ui.run()