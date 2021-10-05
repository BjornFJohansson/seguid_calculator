# Seguid_calculator

![seguid_calculator_small.png](seguid_calculator_small.png "seguid_calculator")

Seguid calculator is a small GUI for calculating the SEGUID, lSEGUID and cSEGUID checksums for a
biological sequence (DNA, RNA or protein).

## Installation

Executables are available from here: [releases](https://github.com/BjornFJohansson/seguid_calculator/releases):

* Windows 64 bit
* Mac OSX app
* Linux DEB and RPM packages are planned (see end of this page)

These packages are build automatically, see the end of this page  for details.

## Source installation

setuptools (pip) or conda packages can be installed like this:

    pip install seguid_calculator

This should work well on Windows and MacOSX. On Linux, wxpython has to be installed separately.

Alternatively, there is a conda package that should install on all platforms on python 3.5, 3.6 or 3.7:

    conda install -c bjornfjohansson seguid_calculator

Visit the website [Bjorn Johansson's group at CBMA](https://metabolicengineeringgroupcbma.github.io/) for more information.

## What does it do ?

The SEGUID checksum is defined as the [SHA-1](http://en.wikipedia.org/wiki/SHA-1) cryptographic hash of a
primary biological sequence in uppercase. SEGUID was suggested by [Babnigg and Giometti ](http://www.ncbi.nlm.nih.gov/pubmed/16858731)
as a way to provide stable identifiers of protein sequences in databases for cross referencing.

There are several implementations of SEGUID calculation available, such as the one in [Biopython](http://biopython.org/wiki/Main_Page).
[Bio.SeqUtils.CheckSum](http://biopython.org/DIST/docs/api/Bio.SeqUtils.CheckSum-module.html).
See [slides](http://precedings.nature.com/documents/278/version/1) and the Biopython
[wiki](http://www.biopython.org/wiki/SeqIO#Using_the_SEGUID_checksum).
See also this blog [post](http://wiki.christophchamp.com/index.php/SEGUID) on the subject.

The lSEGUID is the SEGUID of the lexicographically smallest of the sense or anti-sense strands of a blunt double stranded DNA sequence. This means
that if a sequence and its reverse compliment have the same lSEGUIDs. This can be useful to identify double stranded DNA sequences,
regardless of the form they are presented.

Circular SEGUID or cSEGUID is the SEGUID checksum for circular (DNA) sequences. As there are many permutations
of a circular sequence, the use of the SEGUID checksum directly is impractical as there would be many checksums for the
same sequence.The cSEGUID is the SEGUID of the [lexicographically minimal string rotation](http://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation)
of a sequence or its reverse complement (whichever is smaller).
The cSEGUID provide a unique and stable identifier for circular sequences, such as [plasmids](http://en.wikipedia.org/wiki/Plasmid).

## Example

The cSEGUID checksum can be useful to quickly determine if two sequences refer to the same vector.
The sequence of the plasmid pFA6a-GFPS65T-kanMX6 is available from [Genbank](http://www.ncbi.nlm.nih.gov/nuccore/AJ002682)
and from other sources such as the [Forsburg lab](http://www-bcf.usc.edu/~forsburg/), sequence [here](http://www-bcf.usc.edu/~forsburg/GFPS65T.html) or [here](https://gist.github.com/BjornFJohansson/d394362134338d5f1ff0).

Both sequences are the same size and claim to describe the same vector, although the origins seem to have been set differently.
Analysis of both sequences in seguid_calculator proves that both sequences are in fact representations of the same sequence
by their identical cSEGUIDs:

#### Genbank

![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/genbank.png "seguid_calculator")

#### Forsburg

![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/forsburg.png "seguid_calculator")

## Implementation

Seguid_calculator is written in python 3 with wxPython 4.
Development happens on [Github](https://github.com/BjornFJohansson/seguid_calculator).

## Automatic build status


I will try to set up [packager.io](https://packager.io/gh/BjornFJohansson/seguid_calculator)
to build DEB packages for Linux (work in progress).
