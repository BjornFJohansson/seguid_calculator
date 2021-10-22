#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from seguid_calculator.functions import seqfilter
from seguid_calculator.functions import seguid
from seguid_calculator.functions import rc
from seguid_calculator.functions import SmallestRotation
from seguid_calculator.functions import cseguid
from seguid_calculator.functions import lseguid

from string import ascii_letters
from string import punctuation
from string import digits


def test_seqfilter():

    assert seqfilter(ascii_letters) == ascii_letters
    assert seqfilter(ascii_letters+punctuation+digits) == ascii_letters


def test_seguid():
    assert seguid("A") == seguid("a") == "bc1M4j2I4u6VaLpUbAB8Y9kTHBs"


def test_rc():
    assert rc("gattc") == 'gaatc'


def test_SmallestRotation():
    assert SmallestRotation("gaatc") == 'aatcg'


def test_cseguid():
    assert cseguid("gattc") == seguid("aatcg")


def test_lseguid():
    assert lseguid("gattc") == seguid("gaatc")


if __name__ == "__main__":
    pytest.main([__file__, "-vv", "-s"])
