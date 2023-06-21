import pytest
from seguids import useguid
from seguids import lseguid_blunt
from seguids import lseguid_sticky
from seguids import cseguid

x = "tcgcgcgtttcggtgatgacggtgAAAAcctctgacacatgcagctcccggattgtactgagagtgc"

def test_useguid():

    assert useguid(x) == "cl5ukSUdlvZeBaBLEUhxisdRaL8"
    assert useguid(x.upper()) == "cl5ukSUdlvZeBaBLEUhxisdRaL8"
    assert useguid(x.lower()) == "cl5ukSUdlvZeBaBLEUhxisdRaL8"

def test_lseguid_blunt():

    assert lseguid_blunt(x) == "bHrqalTJ793oAigMQ5_qCttJRTk"

def test_cseguid():

    assert cseguid(x) == "naaZmDzyMa58OsNXROe5SvjC7WU"
    assert cseguid(x) == cseguid(x.upper())
    assert cseguid(x) == cseguid(x.lower())

if __name__ == "__main__":
    pytest.main([__file__, "-vv", "-s"])
