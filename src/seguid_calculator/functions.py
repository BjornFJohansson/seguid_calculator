#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 08:13:13 2021

@author: bjorn
"""
import hashlib
import base64


def seqfilter(seq):
    """doctring."""
    return "".join([b for b in seq if b in
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    "abcdefghijklmnopqrstuvwxyz"])


def useguid(seq):
    """doctring."""
    m = hashlib.sha1()
    m.update(seq.upper().encode())
    return base64.urlsafe_b64encode(m.digest()).decode().rstrip("=")


tab = str.maketrans("GATCRYWSMKHBVDNgatcrywsmkhbvdn",
                    "CTAGYRWSKMDVBHNctagyrwskmdvbhn")


def rc(s):
    """doctring."""
    return s.translate(tab)[::-1]


def SmallestRotation(s):
    """Find the rotation of s that is smallest in lexicographic order.

    Algorithm according to Duval 1983:

    Pierre Duval, Jean. 1983. “Factorizing Words over an Ordered Alphabet.”
    Journal of Algorithms & Computational Technology* 4 (4) (December 1):
    363–381.

    Algorithms on strings and sequences based on Lyndon words.
    David Eppstein, October 2011.

    https://gist.github.com/dvberkel/1950267
    """
    prev, rep = None, 0
    ds = 2 * s
    lens = len(s)
    lends = 2 * lens
    old = 0
    k = 0
    w = ""
    while k < lends:
        i, j = k, k + 1
        while j < lends and ds[i] <= ds[j]:
            i = (ds[i] == ds[j]) and i + 1 or k
            j += 1
        while k < i + 1:
            k += j - i
            prev = w
            w = ds[old:k]
            old = k
            if w == prev:
                rep += 1
            else:
                prev, rep = w, 1
            if len(w) * rep == lens:
                return w * rep
    raise Exception("No shortest rotation")


def cseguid(seq):
    """doctring."""
    return useguid(min(SmallestRotation(str(seq).upper()),
                       SmallestRotation(str(rc(seq)).upper())))


def lseguid(seq):
    """doctring."""
    return useguid(min(str(seq).upper(), str(rc(seq)).upper()))
