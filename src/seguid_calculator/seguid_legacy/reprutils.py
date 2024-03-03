# from seguid.tables import COMPLEMENT_TABLE_DNA
# from textwrap import dedent
from inspect import cleandoc
from .asserts import assert_in_alphabet
from .asserts import assert_anneal
from .manip import reverse
from .tables import tablefactory

def tuple_from_repr(
    rpr: str,
    table: str = "{DNA}",
    space: str = "-"
) -> tuple:
    """Generate a (watson, crick, overhang) tuple from dsDNA text representation.

    This function can generate a tuple (watson, crick, overhang)
    from a dsDNA figure such as the ones depicted below. The resulting
    tuple can be used as an argument for the lSEGUID_sticky or nseguid
    functions. See these functions for the definition of watson, crick and
    overhang. Example inputs can be:
    ::

              -TATGCC
              CATACG-


              GTATGCC
              CATACGG


              GTATGC-
              -ATACGG


    The first and last figure above represent DNA with single
    stranded ends, 3' and 5' respectively. The dash represent
    an empty space in the DNA sequence. This is only allowed
    on one of the adjacent positions. The following is *not*
    allowed:
    ::

              -TATGCC
              -ATACGG


    Examples
    --------
    >>> rpr1 = \"""-TATGCC
    ...           CATACG-\"""
    >>> tuple_from_repr(rpr1)
    ('TATGCC', 'GCATAC', 1)
    >>> rpr2 = \"""GTATGCC
    ...            CATACGG\"""
    >>> tuple_from_repr(rpr2)
    ('GTATGCC', 'GGCATAC', 0)
    >>> rpr3 = \"""GTATGC-
    ...            -ATACGG\"""
    >>> tuple_from_repr(rpr3)
    ('GTATGC', 'GGCATA', -1)
    """
    assert isinstance(space, str)
    assert len(space) == 1
    assert space != " ", "Space can not be 'space' (ASCII 32)"
    linebreak = "\n"

    tabledict = tablefactory(table)

    try:
        assert_in_alphabet(space, alphabet=set(tabledict.keys()) | set(linebreak))
    except ValueError:
        pass
    else:
        ValueError(f"space was set to {space} which is already in the alphabet")

    cleaned_rpr = cleandoc(rpr)

    assert_in_alphabet(cleaned_rpr,
                       alphabet=set(tabledict.keys()) | set(space) | set(linebreak))

    watson, crickrv = cleaned_rpr.splitlines()

    assert len(watson) == len(crickrv)
    assert not (watson.startswith(space) and crickrv.startswith(space))
    assert not (watson.endswith(space) and crickrv.endswith(space))

    overhang = (
        len(watson) - len(watson.lstrip(space)) - (len(crickrv) - len(crickrv.lstrip(space)))
    )

    result = watson.strip(space), crickrv.strip(space)[::-1], overhang
    assert_anneal(*result, table={**tabledict, **{space: space}})

    return result


def repr_from_tuple(
    watson: str,
    crick: str,
    overhang: int,
    table: str = "{DNA}",
    space: str = "-"
) -> str:
    """docstring."""
    assert_anneal(watson, crick, overhang=overhang, table = tablefactory(table))
    assert isinstance(space, str)
    assert len(space) == 1

    msg = (
        f"{overhang*space}{watson}{space*(-overhang+len(crick)-len(watson))}"
        "\n"
        f"{-overhang*space}{reverse(crick)}{space*(overhang+len(watson)-len(crick))}"
    ).rstrip()

    return msg
