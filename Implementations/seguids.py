#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MIT License.

Copyright (c) 2023 Björn Johansson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import hashlib
import base64

# The DNA complement can handle RNA (U>A)

ambiguous_dna_complement = {
    "A": "T", "C": "G", "G": "C",
    "T": "A", "M": "K", "R": "Y",
    "W": "W", "S": "S", "Y": "R",
    "K": "M", "V": "B", "H": "D",
    "D": "H", "B": "V", "X": "X",
    "N": "N", "U": "A",
}

_keys = "".join(ambiguous_dna_complement.keys())
_values = "".join(ambiguous_dna_complement.values())
_complement_table = str.maketrans(_keys + _keys.lower(),
                                  _values + _values.lower())

def seguid(seq: str) -> str:
    """Return the SEGUID (string) for a sequence (string).

    Given a nucleotide or amino-acid sequence (or any string),
    returns the SEGUID string (SEquence Globally Unique IDentifier).
    seq type = str.

    Note that the case is not important:

    >>> seguid("ACGTACGTACGT")
    'If6HIvcnRSQDVNiAoefAzySc6i4'
    >>> seguid("acgtACGTacgt")
    'If6HIvcnRSQDVNiAoefAzySc6i4'

    For more information about SEGUID, see:
    https://doi.org/10.1002/pmic.200600032
    """
    m = hashlib.sha1()
    m.update(seq.encode().upper())
    hsh = base64.encodebytes(m.digest())
    return hsh.decode().rstrip("\n").rstrip("=")


def smallest_rotation(s):
    """Smallest rotation of a string.

    Rapid implementation in C
    """
    from pydivsufsort import min_rotation
    k = min_rotation(s)
    return s[k:] + s[:k]


def rc(sequence: str):
    """Reverse complement.

    accepts mixed DNA/RNA
    """
    return sequence.translate(_complement_table)[::-1]


def useguid(seq: str) -> str:
    """Url safe SEGUID checksum for the sequence.

    This is the SEGUID checksum with the '+' and '/' characters of standard
    Base64 encoding are respectively replaced by '-' and '_'.

    Examples
    --------
    >>> from pydna.utils import useguid
    >>> useguid("aaa")
    'YG7G6b2Kj_KtFOX63j8mRHHoIlE'
    """
    return seguid(seq).replace("+", "-").replace("/", "_")


def lseguid_blunt(seq: str) -> str:
    """Linear SEGUID checksum (lSEGUID).

    Seq represents a blunt double stranded DNA molecule.
    """
    return useguid(min(seq.upper(), str(rc(seq)).upper()))


def lseguid_sticky(watson: str, crick: str, overhang: int) -> str:
    """Linear SEGUID (lSEGUID) checksum.

    Calculates the lSEGUID checksum for a double stranded DNA sequence
    described by two strings (watson and crick) representing the two
    complementary DNA strands and an integer describing the stagger
    between the two strands in the 5' end.

    The overhang is defined as the amount of 3' overhang in the 5'
    side of the molecule. A molecule with 5' overhang has a negative
    value. See examples below:

        dsDNA    ovhg

          nnn...    2
        nnnnn...

         nnnn...    1
        nnnnn...

        nnnnn...    0
        nnnnn...

        nnnnn...   -1
         nnnn...

        nnnnn...   -2
          nnn...


    """
    watson = watson.upper()
    crick = crick.upper()
    lw, lc = len(watson), len(crick)
    if overhang == 0 and lw == lc:
        return lseguid_blunt(watson)
    else:
        w, c, o = min(((watson, crick, overhang), (crick, watson, lw - lc + overhang)))

    return useguid(f"{o*chr(32)}{w}\n{-o*chr(32)}{c[::-1]}")


def cseguid(seq: str, fun=smallest_rotation) -> str:
    """Url safe cSEGUID

    The cSEGUID is the uSEGUID checksum calculated for the lexicographically
    minimal string rotation of a DNA sequence. Only defined for circular
    sequences. The fun argument has to take a string as an argument and
    return another string.

    Examples
    --------
    >>> cseguid("attt")
    'oopV-6158nHJqedi8lsshIfcqYA'
    >>> cseguid("ttta")
    'oopV-6158nHJqedi8lsshIfcqYA'
    """
    return useguid(min(fun(seq.upper()), fun(str(rc(seq)).upper())))


def smallest_rotation_py(s):
    """Smallest rotation of a string.

    Algorithm described in Pierre Duval, Jean. 1983. Factorizing Words
    over an Ordered Alphabet. Journal of Algorithms & Computational Technology
    4 (4) (December 1): 363–381. and Algorithms on strings and sequences based
    on Lyndon words, David Eppstein 2011.
    https://gist.github.com/dvberkel/1950267

    This is a pure python implementation, considerably slower than

    Examples
    --------
    >>> smallest_rotation("taaa")
    'aaat'

    """
    from array import array as _array
    prev, rep = None, 0
    ds = _array("u", 2 * s)
    lens, lends = len(s), len(ds)
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
                return "".join(w * rep)


if __name__ == "__main__":
    import timeit

    dna500 = """\
    CAGTGAAATCAGAACCCATGAGGGCGGACGAGTCATATCC
    GGTATTAGAGATTTATACAGTCTGGACACCTAGCGAACCG
    ACTTGAACCACCAGGATTGAAGACGAAACCTTAGAGTATA
    GTAATGCCGTACGTGTCGGGGCCCACGCATCTAGGACAGG
    ATCGCATGATGGTGGTTTTAGTTGCCGTTGTACCGGATTT
    CTTAGTAGTATAAGCATGAGGATAAGTGAAACCGGGTGAA
    GGTGGTTTGTGTGAGTGCCTAATAGTCCGACTCCCCGAGG
    GGAGTAGGCACTGCCTTCAGCGTTCAGTTATTGAGCACGT
    CCGCCCGGCGAAAGATGGCTTTGAGCTCCACTGACAGCCA
    GGGACCGCGTGCATGAGGCTAGAGCAGAGTCGTTGACAGT
    GAGATTAGATTGATCATTTTTATCTGAAACGGCAGCATAC
    CGACAGTTGTTCTCAAGCAAAGTGGTCTTGCCTAGATTCA
    ATATTGCCCACAATCAGCTC""".replace("\n", "")

    print("pure python")
    print(timeit.timeit("cseguid(dna500, fun=smallest_rotation_py)",
                        globals=globals(),
                        number=10000))
    print("pydivsufsort")
    print(timeit.timeit("cseguid(dna500)",
                        globals=globals(),
                        number=10000))
