# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

from seguid import lsseguid as _lsseguid
from seguid import csseguid as _csseguid
from seguid import ldseguid as _ldseguid
from seguid import cdseguid as _cdseguid

tab = str.maketrans("GATCRYWSMKHBVDNgatcrywsmkhbvdn",
                    "CTAGYRWSKMDVBHNctagyrwskmdvbhn")

table = "GC,AT,TA,CG,RY,YR,WW,SS,MK,KM,HD,BV,VB,DH,NN"


def rc(s):
    """doctring."""
    return s.translate(tab)[::-1]


def seqfilter(seq):
    """doctring."""
    return "".join(b for b in seq.upper() if b in "GATCRYWSMKHBVDN")


def lsseguid(s):
    return _lsseguid(s.upper(), alphabet = "{DNA}")


def csseguid(s):
    return _csseguid(s.upper(), alphabet = "{DNA}")


def ldseguid(s):
    return _ldseguid(s.upper(), rc(s.upper()), alphabet = "{DNA}")


def cdseguid(s):
    return _cdseguid(s.upper(), rc(s.upper()), alphabet = "{DNA}")


def calcicon():
    from wx.lib.embeddedimage import PyEmbeddedImage
    return PyEmbeddedImage(
    "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"
    "efXVp054G/8H47hlMPNtUfAAAAAASUVORK5CYII=")
