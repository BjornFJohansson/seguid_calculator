# seguid_calculator

[![Conda Package](https://github.com/BjornFJohansson/seguid_calculator/actions/workflows/build_conda.yml/badge.svg)](https://github.com/BjornFJohansson/seguid_calculator/actions/workflows/build_conda.yml)
[![Setuptools Package](https://github.com/BjornFJohansson/seguid_calculator/actions/workflows/build_setuptools.yml/badge.svg)](https://github.com/BjornFJohansson/seguid_calculator/actions/workflows/build_setuptools.yml)
[![Pytest](https://github.com/BjornFJohansson/seguid_calculator/actions/workflows/test.yml/badge.svg)](https://github.com/BjornFJohansson/seguid_calculator/actions/workflows/test.yml)
[![Pyinstaller](https://github.com/BjornFJohansson/seguid_calculator/actions/workflows/pyinstaller.yml/badge.svg?branch=master)](https://github.com/BjornFJohansson/seguid_calculator/actions/workflows/pyinstaller.yml)

![seguid_calculator_small.png](seguid_calculator_small.png "seguid_calculator")

Seguid_calculator is a small GUI for calculating the SEGUID, lSEGUID and cSEGUID checksums for a
biological sequence (DNA, RNA or protein).

## Installation

The quickest way to use seguid_calculator is by downloading one of the executables, there requre no installation at all. Executables are available from here: [releases](https://github.com/BjornFJohansson/seguid_calculator/releases):

- **seguid_calculator.exe** for Windows
- **seguid_calculator_for_mac.zip** for MacOS
- **seguid_calculator** is an executable for Linux
- No DEB or RPM packages yet (these are a planned feature for when I figure out how to make them)

These packages are built automatically using Github actions. There is also an online version (see links at the end of this page.

## Source installation

setuptools (pip) can be installed like this:

    pip install seguid_calculator

This should work well on Windows and MacOSX. On Linux, wxpython may have to be installed separately.

Alternatively, there is a conda package that should install on all platforms on python 3.7, 3.8 or 3.9:

    conda install -c bjornfjohansson seguid_calculator

For this, you need to install the [anaconda scientific python distribution](https://www.anaconda.com/products/individual).

## What does it do ?

The SEGUID checksum is defined as the [SHA-1](http://en.wikipedia.org/wiki/SHA-1) cryptographic hash of a
primary biological sequence in uppercase. SEGUID was suggested by [Babnigg and Giometti ](http://www.ncbi.nlm.nih.gov/pubmed/16858731)
as a way to provide stable identifiers of protein sequences in databases for cross referencing.

There are several implementations of SEGUID calculation available, such as the one in [Biopython](http://biopython.org/wiki/Main_Page).
[Bio.SeqUtils.CheckSum](http://biopython.org/DIST/docs/api/Bio.SeqUtils.CheckSum-module.html).
See [slides](https://www.nature.com/articles/npre.2007.278.1) and the Biopython
[wiki](https://biopython.org/wiki/SeqIO#Using_the_SEGUID_checksum).

See also this blog [post](http://wiki.christophchamp.com/index.php/SEGUID) on the subject.

## cSEGUID

Circular SEGUID or cSEGUID is the SEGUID checksum for circular (DNA) sequences. As there are many permutations
of a circular sequence, the use of the SEGUID checksum directly is impractical as there would be many checksums for the different permutations of the
same circular sequence. The cSEGUID is instead defined as the SEGUID of the [lexicographically minimal string rotation](http://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation)
of a sequence or its reverse complement (whichever is lexicographically smaller). 

The cSEGUID provide a unique and stable identifier for circular sequences, such as [plasmids](http://en.wikipedia.org/wiki/Plasmid).

### Example

The cSEGUID checksum can be useful to quickly determine if two sequences refer to the same vector.
The sequence of the plasmid pFA6a-GFPS65T-kanMX6 is available from [Genbank](http://www.ncbi.nlm.nih.gov/nuccore/AJ002682)
and from other sources such as the [Forsburg lab](http://www-bcf.usc.edu/~forsburg/), sequence [here](http://www-bcf.usc.edu/~forsburg/GFPS65T.html), a copy of which was saved [here](https://gist.github.com/BjornFJohansson/d394362134338d5f1ff0).

Both sequences are the same size and claim to describe the same vector. Analysis of both sequences in seguid_calculator proves that both sequences are in fact representations of the same sequence by their identical cSEGUIDs:

#### Genbank

![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/genbank.png "seguid_calculator")

#### Forsburg

![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/forsburg.png "seguid_calculator")

## lSEGUID

The lSEGUID is the SEGUID of the lexicographically smallest of the sense or anti-sense strands of a blunt double stranded DNA sequence. This can be useful to identify double stranded DNA sequences, regardless of the form they are presented.

## Implementation

Seguid_calculator is written in python 3 with wxPython 4 which is the only dependence. Development happens on [Github](https://github.com/BjornFJohansson/seguid_calculator).

## Online version

There is also an online version built with [flask](https://github.com/pallets/flask) and hosted on [pythonanywhere](https://www.pythonanywhere.com/).

[![seguid_calculator_flask](seguid_calculator_flask.png)](http://seguidcalculator.pythonanywhere.com/)

Click [here](http://seguidcalculator.pythonanywhere.com/) or on the image above to take you to the website.
