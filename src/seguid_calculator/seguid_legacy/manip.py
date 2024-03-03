#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from array import array
from typing import Callable

from .asserts import assert_table
from .asserts import assert_in_alphabet
from .tables import COMPLEMENT_TABLE_DNA


def rotate(seq: str, amount: int = 0) -> str:
    """Rotates a circular, DNA sequence a certain amount.

    Rotates sequence 'seq', 'amount' number of symbols to the right.
    A rotation 'amount' is the same as a rotation 'amount + n * len(seq)'
    for any integer 'n'.

    Returns the rotated sequence as a string of length 'len(seq)'.

    Examples
    --------
    >>> seq = "ABCDEFGH"
    >>> rotate(seq, 0)
    'ABCDEFGH'

    >>> rotate(seq, +1)
    'BCDEFGHA'

    >>> rotate(seq, +7)
    'HABCDEFG'

    >>> rotate(seq, -1)
    'HABCDEFG'

    >>> rotate(seq, +8)
    'ABCDEFGH'
    """
    assert isinstance(seq, str), "Argument 'seq' must be an string"
    assert isinstance(amount, int), "Argument 'amount' must be an integer"

    ## Nothing to rotate?
    if len(seq) == 0:
        return seq

    amount = amount % len(seq)

    ## Rotate?
    if amount > 0:
        seq = seq[amount:] + seq[:amount]

    return seq


def complementary(seq: str, table: dict = COMPLEMENT_TABLE_DNA) -> str:
    """Complement of a DNA sequence."""
    ## Validate 'table':
    assert_table(table)

    ## Validate 'seq':
    assert_in_alphabet(seq, alphabet=set(table.keys()))

    return seq.translate({ord(k): ord(v) for k, v in table.items()})


def reverse(seq) -> str:
    """Reverses a DNA sequence"""
    assert isinstance(seq, str), "Argument 'seq' must be an string"
    return seq[::-1]


def rc(seq: str, table: dict = COMPLEMENT_TABLE_DNA) -> str:
    """Reverse complement of sequence.

    Returns the reverse complement for a DNA strand.

    The default complement table accepts GATC only.

    The tables module defines and alternative table containing the
    ambiguous codes suggested by IUPAC.

    Examples
    --------
    >>> rc("GTT")
    'AAC'
    >>> from seguid.manip import rc
    >>> rc("GTa")
    Traceback (most recent call last):
        ...
    ValueError: Detected symbols a in not in the 'alphabet'
    >>> rc("GTa".upper())
    'TAC'
    """
    return reverse(complementary(seq, table=table))


def min_rotation_py(s: str) -> int:
    """Start position for the smallest rotation of a string s (pure Python).

    Algorithm described in:

    Pierre Duval, Jean. 1983. Factorizing Words
    over an Ordered Alphabet. Journal of Algorithms & Computational Technology
    4 (4) (December 1): 363–381. and Algorithms on strings and sequences based
    on Lyndon words, David Eppstein 2011.
    https://gist.github.com/dvberkel/1950267

    This is a pure python implementation, considerably slower than the
    min_rotation function from pydivsufsort that is imported at the top of
    this script.

    Should only be used if pydivsufsort.min_rotation can not be used.

    Note that both functions are case-sensitive and sorts by ASCII-code order
    or "ASCIIbetical" order so:

    - Uppercase come before lowercase letters; for example, "Z" precedes "a"
    - Digits and several punctuation marks come before letters.

    See the last two examples below for an example of the consequences of this.

    Examples
    --------
    >>> min_rotation_py("TAAA")
    1
    >>> "TAAA"[1:] + "TAAA"[:1]
    'AAAT'
    >>> s = "ACAACAAACAACACAAACAAACACAAC"
    >>> min_rotation_py(s)
    14
    >>> s[14:] + s[:14]
    'AAACAAACACAACACAACAAACAACAC'
    """

    prev, rep = None, 0
    ds = array("u", 2 * s)
    lens = len(s)
    lends = lens * 2
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
                return old - i
    return 0


def rotate_to_min(s: str) -> int:
    from seguid.config import _min_rotation

    ## Assert upper-case letters are ordered before lower-case letters
    assert _min_rotation("Aa") == 0

    amount = _min_rotation(s)
    s = rotate(s, amount=amount)
    return s


# def linearize_circular_dsDNA(watson, crick, position):
#     cposition = len(watson) - position
#     swatson = watson[position:] + watson[:position]
#     scrick = watson[cposition:] + watson[:cposition]
#     return (swatson, scrick, 0)
