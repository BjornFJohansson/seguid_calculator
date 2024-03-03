#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .tables import COMPLEMENT_TABLE_DNA
from string import ascii_letters
from string import digits
import re

def assert_in_alphabet(seq: str,
                       alphabet: set):

    assert isinstance(seq, str), "Argument 'seq' must be an string"
    assert isinstance(alphabet, set), "Argument 'alphabet' must be a set"
    assert len(alphabet) > 0, "Argument 'alphabet' must not be empty"
    assert not alphabet - (set(ascii_letters) | set(digits) | set("\n-")), "Only A-Z a-z allowed"
    first = list(alphabet)[0]
    assert isinstance(first, str), "Argument 'alphabet' should contain 'str' elements"

    # Nothing to do?
    if len(seq) == 0:
        return

    unknown = set(
        c for c in seq if c not in (k for k in alphabet)
    )

    if unknown:
        missing = ' '.join(unknown)
        raise ValueError(
            "Detected symbols " f"{missing} in not in the 'alphabet'"
        )


def assert_table(table: dict):
    assert isinstance(table, dict), "Argument 'table' must be a dict"
    keys  = table.keys()
    values = table.values()
    # Assert that the set of values are also in the set of keys
    unknown = set(
        chr(v) for v in values if v not in (k for k in keys)
    )

    if unknown:
        missing = ' '.join(unknown)
        raise ValueError(
            "Detected values (" f"{missing}) in 'table' that are not in the keys"
        )


def assert_anneal(watson: str,
                  crick: str,
                  overhang: int,
                  table: dict = COMPLEMENT_TABLE_DNA) -> bool:
    """docstring."""
    from seguid_calculator.seguid_legacy.manip import rc
    assert_table(table)
    assert_in_alphabet(watson, alphabet=set(table.keys()))
    assert_in_alphabet(crick, alphabet=set(table.keys()))

    assert isinstance(overhang, int), "overhang must be an integer"
    assert -len(watson) < overhang, "watson and crick has to anneal with at least one bp"
    assert overhang < len(crick), "watson and crick has to anneal with at least one bp"

    up = watson[max(-overhang, 0): len(crick) - overhang]
    dn = rc(crick, table=table)[max(overhang, 0): len(watson) + overhang]

    if up != dn:
        raise ValueError("Mismatched basepairs.")


# def assert_checksum(checksum):
#     checksum = "cdseguid:AWD-dt5-TEua8RbOWfnctJIu9nA"
#     mobj = re.match("(?:|sl|sc|ds|dc)seguid:(.+)", checksum)
#     assert len(mobj.group(1)) == 27
#     b64 = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/_-')
#     assert set(mobj.group(1)).issubset(b64)
