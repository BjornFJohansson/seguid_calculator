This is a small GUI application to calculate the seguid and cseguid
checksums for biological sequences (DNA, RNA or protein). The seguid
checksum is the `SHA-1 <http://en.wikipedia.org/wiki/SHA-1>`__
cryptographic hash of the primary biological sequence in uppercase.
seguid was suggested by `Babnigg and
Giometti <http://www.ncbi.nlm.nih.gov/pubmed/16858731>`__ to provide
stable identifiers of protein sequences in databases for cross
referencing.

Circular sequences of double stranded DNA can be uniquely identified by
the cseguid checksum. The `lexicographically minimal string
rotation <http://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation>`__
in uppercase is calculated for a sequence and its reverse complement.
The cseguid is the seguid of the smallest of the two and provide a
unique and stable identifier for circular sequence, such as
`plasmids <http://en.wikipedia.org/wiki/Plasmid>`__.

Visit the website `Björn Johansson's group at
CBMA <https://sites.google.com/site/metabolicengineeringgroup/>`__ for
more information.
