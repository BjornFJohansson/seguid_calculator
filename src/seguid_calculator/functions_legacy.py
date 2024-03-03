# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

from .seguid_legacy.chksum import lsseguid as _lsseguid
from .seguid_legacy.chksum import csseguid as _csseguid
from .seguid_legacy.chksum import ldseguid as _ldseguid
from .seguid_legacy.chksum import cdseguid as _cdseguid

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
    """doctring."""
    return _lsseguid(s.upper(), table=table)


def csseguid(s):
    """doctring."""
    return _csseguid(s.upper(), table=table)


def ldseguid(s):
    """doctring."""
    return _ldseguid(s.upper(), rc(s.upper()), 0,table=table)


def cdseguid(s):
    """doctring."""
    return _cdseguid(s.upper(), rc(s.upper()), table=table)
