# seguid_calculator
![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/calculator.png "seguid_calculator")Seguid calculator is a small GUI application for calculating the SEGUID, lSEGUID and cSEGUID checksums for a 
biological sequence (DNA, RNA or protein). 
It is available as executables for Windows, MacOSX and Linux (see below).

The SEGUID checksum is defined as the [SHA-1](http://en.wikipedia.org/wiki/SHA-1) cryptographic hash of a 
primary biological sequence in uppercase. SEGUID was suggested by [Babnigg and Giometti ](http://www.ncbi.nlm.nih.gov/pubmed/16858731) 
as a way to provide stable identifiers of protein sequences in databases for cross referencing.

There are several implementations of SEGUID calculation available, such as the one in [Biopython](http://biopython.org/wiki/Main_Page).
[Bio.SeqUtils.CheckSum](http://biopython.org/DIST/docs/api/Bio.SeqUtils.CheckSum-module.html). 
See [slides](http://precedings.nature.com/documents/278/version/1) and the Biopython 
[wiki](http://www.biopython.org/wiki/SeqIO#Using_the_SEGUID_checksum). 
See also this blog [post](http://wiki.christophchamp.com/index.php/SEGUID) on the subject.

The lSEGUID is the SEGUID of the lexocographically smallest of the sense or antisense strands of a double stranded DNA sequence. This means
that if a sequence and its reverse compliment have the same lSEGUIDs. This can be useful to identify double stranded DNA sequences, 
regardless of the form they are presented. 

Circular SEGUID or cSEGUID is the SEGUID checksum for circular (DNA) sequences. As there are many circular permutations 
of a circular sequence, the use of the SEGUID checksum directly is impractical as there would be many checksums for the 
same sequence.The cSEGUID is the SEGUID of the [lexicographically minimal string rotation](http://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation) 
of a sequence or its reverse complement (whichever is [lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) smaller). 
The cSEGUID provide a unique and stable identifier for circular sequence, such as [plasmids](http://en.wikipedia.org/wiki/Plasmid).

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
Seguid_calculator is written in python 2.7 with wxPython 3. Development happens on [Github](https://github.com/BjornFJohansson/seguid_calculator) where source code is available.

## Executables

Executables are available for

* Windows 64 bit
* Mac OSX dmg and a zip file containing an app
* Linux deb package

The executables can be downloaded from the button at the top of this page 
called [releases](https://github.com/BjornFJohansson/seguid_calculator/releases).

Visit the website [Bjorn Johansson's group at CBMA](https://sites.google.com/site/metabolicengineeringgroup/) for more
 information.

## Automatic build status

Windows standalone executables (32 and 64 bit) are built on [AppVeyor](https://ci.appveyor.com/project/BjornFJohansson/seguid-calculator) using [pyinstaller](http://www.pyinstaller.org/) and [Miniconda](http://conda.pydata.org/miniconda.html).

[![Build status](https://ci.appveyor.com/api/projects/status/0bd4f7fi3g0m0itp?svg=true)](https://ci.appveyor.com/project/BjornFJohansson/seguid-calculator)

Standalone executables (64 bit) for MacOSX are built on [TravisCI](https://travis-ci.org/BjornFJohansson/seguid_calculator) using [pyinstaller](http://www.pyinstaller.org/) and [Miniconda](http://conda.pydata.org/miniconda.html).
 
[![Build Status](https://travis-ci.org/BjornFJohansson/seguid_calculator.svg?branch=master)](https://travis-ci.org/BjornFJohansson/seguid_calculator)

A debian package (.deb) is built offline, currently on Ubuntu 16.04 using [stdeb](https://github.com/astraw/stdeb). Look at the script "run_this_scritp_to_create_deb_package.sh". 
This installs system shorcuts as well.





