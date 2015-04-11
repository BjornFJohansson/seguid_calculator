#![alt text](BjornFJohansson/seguid_calculator/blob/master/calculator.png "seguid_calculator") seguid-calculator

Is a small GUI application to calculate the SEGUID and cSEGUID checksums for a biological sequence (DNA, RNA or protein). The SEGUID checksum is the [SHA-1](http://en.wikipedia.org/wiki/SHA-1) cryptographic hash of the primary biological sequence in uppercase. SEGUID was developed by [Babnigg and Giometti ](http://www.ncbi.nlm.nih.gov/pubmed/16858731) to provide stable identifiers of protein sequences in databases for cross referencing.

cSEGUID is the SEGUID for circular sequences. cSEGUID is the SEGUID of the [lexicographically minimal string rotation](http://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation) of a sequence or the reverse complement of the sequence. The cSEGUID provide a unique and stable identifier for circular sequence, such as [plasmids](http://en.wikipedia.org/wiki/Plasmid).


Seguid-calculator is written in python 2.7 with wxPython 3.0.2. Seguid-calculator is available as source code, a windows executable made with Pyinstaller and an old Jython/Swing version that should work on any platform with a Java runtime environment.

Visit the website [Björn Johansson's group at CBMA](https://sites.google.com/site/metabolicengineeringgroup/) for more information.
