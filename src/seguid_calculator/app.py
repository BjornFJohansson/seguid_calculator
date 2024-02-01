#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring."""
from string import ascii_letters

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from seguid_calculator.functions import seqfilter
from seguid_calculator.functions import rc
from seguid_calculator.functions import lsseguid
from seguid_calculator.functions import csseguid
from seguid_calculator.functions import ldseguid
from seguid_calculator.functions import cdseguid
from seguid_calculator.functions import calcicon

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful_secretkey",
    WTF_CSRF_SECRET_KEY="a_csrf_secret_key"))

@app.route("/", methods=["GET", "POST"])
def index():
    """docstring."""
    if request.method == "GET":
        return render_template("index.html")

    sequence = seqfilter(request.form.get("sequence") or "")

    if 'calc' in request.form:
        pass
    elif 'reverse' in request.form:
        sequence = sequence[::-1]
    elif 'complement' in request.form:
        sequence = rc(sequence)[::-1]
    elif 'reverse_complement' in request.form:
        sequence = rc(sequence)
    elif 'clear' in request.form:
        return redirect(url_for('index'))

    if sequence:
        slseg = lsseguid(sequence)
        scseg = csseguid(sequence)
        dlseg = ldseguid(sequence)
        dcseg = cdseguid(sequence)
    else:
        slseg = ""
        scseg = ""
        dlseg = ""
        dcseg = ""
    return render_template("index.html",
                           lsseguid=slseg,
                           csseguid=scseg,
                           ldseguid=dlseg,
                           cdseguid=dcseg,
                           length=len(sequence) or "",
                           characters=" ".join(sorted(set(sequence.upper()))),
                           sequence=sequence)


if __name__ == '__main__':
    from webui import WebUI
    ui = WebUI(app, debug=True)
    ui.run()
