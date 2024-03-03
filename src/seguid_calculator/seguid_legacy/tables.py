#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition of Complementary DNA Symbols
COMPLEMENT_TABLE_DNA = {"G": "C",
                        "A": "T",
                        "C": "G",
                        "T": "A"}


# Definition of Complementary RNA Symbols
COMPLEMENT_TABLE_RNA = {"G": "C",
                        "A": "U",
                        "C": "G",
                        "U": "A"}


# Definition of Complementary IUPAC Ambigous DNA Symbols
"""
The table below was adapted from Cornish-Bowden, 1985:

======== ================== ============ ======================================
Symbol   Meaning            Complement   Origin of designation
======== ================== ============ ======================================
 G        G                  C            Guanine
 A        A                  T            Adenine
 T        T                  A            Thymine
 C        C                  G            Cytosine
 R        A or G             Y            puRine
 Y        C or T             R            pYrimidine
 M        A or C             K            aMino
 K        G or T             M            Ketone
 S        C or G             S            Strong interaction (3 H bonds)
 W        A or T             W            Weak interaction (2 H bonds)
 H        A or C or T        D            not-G, H (follows G in the alphabet)
 B        C or G or T        V            not-A, B follows A
 V        A or C or G        B            not-T (not-U), V follows U
 D        A or G or T        H            not-C, D follows C
 N        G or A or T or C   N            aNy
======== ================== ============ ======================================


Cornish-Bowden, A. (1985). Nomenclature for incompletely specified
bases in nucleic acid sequences: recommendations 1984.
Nucleic Acids Research, 13(9), 3021–3030.
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC341218
"""

COMPLEMENT_TABLE_IUPAC = {**COMPLEMENT_TABLE_DNA,  **{"B": "V",
                                                      "D": "H",
                                                      "H": "D",
                                                      "K": "M",
                                                      "M": "K",
                                                      "S": "S",
                                                      "R": "Y",
                                                      "V": "B",
                                                      "Y": "R",
                                                      "W": "W",
                                                      "N": "N"}}

# Definition of a the IUPAC Protein Symbols
# values are empty strings since there is no concept of complementarity
# for proteins
TABLE_IUPAC_PROTEIN = {"A": "",
                       "C": "",
                       "D": "",
                       "E": "",
                       "F": "",
                       "G": "",
                       "H": "",
                       "I": "",
                       "K": "",
                       "L": "",
                       "M": "",
                       "N": "",
                       "P": "",
                       "Q": "",
                       "R": "",
                       "S": "",
                       "T": "",
                       "V": "",
                       "W": "",
                       "Y": ""}


table_categories = {
    "{DNA}": COMPLEMENT_TABLE_DNA,
    "{RNA}": COMPLEMENT_TABLE_RNA,
    "{IUPAC}": COMPLEMENT_TABLE_IUPAC,
    "{protein}": TABLE_IUPAC_PROTEIN,
}


def tablefactory(argument: str):
    # argument = "{protein},X,Z"
    # argument = "{DNA},BV,VB,DH,HD,KM,MK,NN,SS,WW"
    # argument = "AT,TA,CG,GC"
    # argument = 'A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y'
    tb, *ext = [e for e in argument.split(",")]
    try:
        table = table_categories[tb]
    except KeyError:
        if len(tb) == 1:
            table = {tb[0]: ""}
        elif len(tb) == 2:
            table = {tb[0]: tb[1]}
        else:
            raise ValueError("First element not a table category, symbol or basepair.")

    if ext and all(len(e) == 1 for e in ext):
        assert set(table.values()) == {""}  # extension is an alphabet
        table.update((c, "") for c in ext)
    elif ext and all(len(e) == 2 for e in ext):
        # assert_table                      # extension is a translation table
        table.update((k, v) for k, v in ext)
    return table
