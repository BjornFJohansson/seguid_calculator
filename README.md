# seguid_calculator
Seguid calculator is a small GUI application for calculating the SEGUID and cSEGUID checksums for a biological sequence (DNA, RNA or protein). It is available as executables for Windows, MacOSX and Linux (see below).

The SEGUID checksum is defined as the [SHA-1](http://en.wikipedia.org/wiki/SHA-1) cryptographic hash of a primary biological sequence in uppercase. SEGUID was suggested by [Babnigg and Giometti ](http://www.ncbi.nlm.nih.gov/pubmed/16858731) as a way to provide stable identifiers of protein sequences in databases for cross referencing.

There are several implementations of SEGUID calculation available, such as the [Biopython](http://biopython.org/wiki/Main_Page) module
[Bio.SeqUtils.CheckSum](http://biopython.org/DIST/docs/api/Bio.SeqUtils.CheckSum-module.html). See [slides](http://precedings.nature.com/documents/278/version/1) and from the Biopython [wiki](http://www.biopython.org/wiki/SeqIO#Using_the_SEGUID_checksum). See also a blog [post](http://wiki.christophchamp.com/index.php/SEGUID) on the subject.



Circular SEGUID or cSEGUID is the SEGUID checksum for circular (DNA) sequences. As there are many circular permutations of a circular sequence, the use of the SEGUID checksum directly is impractical as there would be many checksums for the same sequence.The cSEGUID is the SEGUID of the [lexicographically minimal string rotation](http://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation) of a sequence or its reverse complement (whichever is [   lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) smaller). The cSEGUID provide a unique and stable identifier for circular sequence, such as [plasmids](http://en.wikipedia.org/wiki/Plasmid).

## Example
The cSEGUID checksum can be useful to quickly determin if two sequences refer to the same vector. The sequence of the plasmid pFA6a-GFPS65T-kanMX6 is available from [Genbank](http://www.ncbi.nlm.nih.gov/nuccore/AJ002682) and from other sources such as the [Forsburg lab](http://www-bcf.usc.edu/~forsburg/), sequence [here](http://www-bcf.usc.edu/~forsburg/GFPS65T.html) or [here](https://gist.github.com/BjornFJohansson/d394362134338d5f1ff0).

Both sequences are the same size and claim to describe the same vector, although the origins seem to be set differently. Analysis of both sequences in seguid_calculator proves that both sequences are in fact representations of the same sequence by their identical cSEGUIDs:

#### Genbank
![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/genbank.png "seguid_calculator") 

#### Forsburg
![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/forsburg.png "seguid_calculator")

## Implementation
Seguid_calculator is written in python 2.7 with wxPython 3. Development happens on [Github](https://github.com/BjornFJohansson/seguid_calculator) where source code is available.

## Executables
![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/calculator.png "seguid_calculator")

Windows executable for 32 bits is available [here](https://ci.appveyor.com/api/buildjobs/mlp0bbvqsnhg382c/artifacts/build/lib/seguid_calculator/dist/seguid_calculator.exe).

Windows executable for 64 bits is available [here](https://ci.appveyor.com/api/buildjobs/johw573mecp7utc9/artifacts/build/lib/seguid_calculator/dist/seguid_calculator.exe).

Mac OS executables executable for 64 bits is available [here]().

Linux executable for 64 bits is available [here]().

Visit the website [Björn Johansson's group at CBMA](https://sites.google.com/site/metabolicengineeringgroup/) for more
 information.

## Automatic build status
 [![Build status](https://ci.appveyor.com/api/projects/status/0bd4f7fi3g0m0itp?svg=true)](https://ci.appveyor.com/project/BjornFJohansson/seguid-calculator)
[![Build Status](https://travis-ci.org/BjornFJohansson/seguid_calculator.svg?branch=master)](https://travis-ci.org/BjornFJohansson/seguid_calculator)
[![Build Status](https://drone.io/github.com/BjornFJohansson/seguid_calculator/status.png)](https://drone.io/github.com/BjornFJohansson/seguid_calculator/latest)
