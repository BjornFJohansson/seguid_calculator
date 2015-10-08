#![alt text](https://raw.githubusercontent.com/BjornFJohansson/seguid_calculator/master/calculator.png "seguid_calculator") seguid_calculator

[![Build status](https://ci.appveyor.com/api/projects/status/0bd4f7fi3g0m0itp?svg=true)](https://ci.appveyor.com/project/BjornFJohansson/seguid-calculator)


[![Build status](https://travis-ci.org/BjornFJohansson/pydna.svg)](https://travis-ci.org/BjornFJohansson/pydna) 


[![Build Status](https://drone.io/github.com/BjornFJohansson/seguid_calculator/status.png)](https://drone.io/github.com/BjornFJohansson/seguid_calculator/latest)

Is a small GUI application to calculate the SEGUID and cSEGUID checksums for a biological sequence (DNA, RNA or protein). 
The SEGUID checksum is the [SHA-1](http://en.wikipedia.org/wiki/SHA-1) cryptographic hash of the primary biological 
sequence in uppercase. SEGUID was suggested by [Babnigg and Giometti ](http://www.ncbi.nlm.nih.gov/pubmed/16858731) 
to provide stable identifiers of protein sequences in databases for cross referencing.

cSEGUID is the SEGUID for circular sequences. cSEGUID is the SEGUID of the 
[lexicographically minimal string rotation](http://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation) 
of a sequence or its reverse complement (whichever is smallest). The cSEGUID provide a unique and stable identifier for 
circular sequence, such as [plasmids](http://en.wikipedia.org/wiki/Plasmid).

Seguid_calculator is written in python 2.7 with wxPython 3.0.2. seguid_calculator is available as 
[source code](), a windows 
executable made with Pyinstaller on [Appveyor](), 
Mac OS executables built on Travis ci and as a [.deb package]() built on Drone.io 
using [stdeb](https://pypi.python.org/pypi/stdeb)


Windows executables can be downloaded [here]

MacOS executables can be downloaded [here](https://github.com/BjornFJohansson/seguid_calculator/releases)

Linux .deb package can be found [here]() 

Visit the website [Björn Johansson's group at CBMA](https://sites.google.com/site/metabolicengineeringgroup/) for more
 information.
