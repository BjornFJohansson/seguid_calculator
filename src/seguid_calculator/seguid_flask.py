#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring."""

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from .functions import seqfilter
from .functions import seguid
from .functions import rc
from .functions import cseguid
from .functions import lseguid

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
        segu = seguid(sequence)
        lseg = lseguid(sequence)
        cseg = cseguid(sequence)
    else:
        segu = ""
        lseg = ""
        cseg = ""
    return render_template("index.html",
                           seguid=segu,
                           lseguid=lseg,
                           cseguid=cseg,
                           length=len(sequence) or "",
                           characters=" ".join(sorted(set(sequence.upper()))),
                           sequence=sequence)

if __name__ == '__main__':
    from webui import WebUI
    ui = WebUI(app, debug=True)
    ui.run()