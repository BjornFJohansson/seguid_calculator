# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

from seguid import lsseguid as _lsseguid
from seguid import csseguid as _csseguid
from seguid import ldseguid as _ldseguid
from seguid import cdseguid as _cdseguid

tab = str.maketrans("GATCRYWSMKHBVDNgatcrywsmkhbvdn",
                    "CTAGYRWSKMDVBHNctagyrwskmdvbhn")

# table = "GC,AT,TA,CG,RY,YR,WW,SS,MK,KM,HD,BV,VB,DH,NN"
alphabet = "GC,AT,BV,DH,KM,SS,RY,WW,NN"

def rc(s):
    """doctring."""
    return s.translate(tab)[::-1]


def seqfilter(seq):
    """doctring."""
    return "".join(b for b in seq.upper() if b in "GATCRYWSMKHBVDN")


def lsseguid(s):
    """doctring."""
    return _lsseguid(s.upper(), alphabet=alphabet)


def csseguid(s):
    """doctring."""
    return _csseguid(s.upper(), alphabet=alphabet)


def ldseguid(s):
    """doctring."""
    return _ldseguid(s.upper(), rc(s.upper()), alphabet=alphabet)


def cdseguid(s):
    """doctring."""
    return _cdseguid(s.upper(), rc(s.upper()), alphabet=alphabet)
