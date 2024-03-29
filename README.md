# seguid_calculator

Seguid_calculator is a flask web app for calculating [seguid](https://www.seguid.org) checksums
for DNA or RNA sequences. Four checksums are defined in the table below with their respective use case.

| name     | topology | strandedness    |
| -------- | -------- | --------------- |
| lsseguid | linear   | single-stranded |
| ldseguid | linear   | double-stranded |
| csseguid | circular | single-stranded |
| cdseguid | circular | double-stranded |

The lsseguid checksum is also useful for protein sequences.

## What does it do ?

SEGUID was suggested by [Babnigg and Giometti ](http://www.ncbi.nlm.nih.gov/pubmed/16858731)
as a stable identifier for cross referencing protein sequences in databases.

## Use case

The cdSEGUID checksum can be useful to determine if two sequences refer to the same circular plasmid vector.
The sequence of the plasmid pFA6a-GFPS65T-kanMX6 is available from [Genbank](http://www.ncbi.nlm.nih.gov/nuccore/AJ002682) and
from other sources on the web such as the [Forsburg lab](https://dornsife.usc.edu/pombenet/), sequence [here](https://dornsife.usc.edu/pombenet/vectors/),
and [here](https://gist.github.com/BjornFJohansson/d394362134338d5f1ff0).

Both sequences are meant to describe the same vector. The sequences are both, 4882 bp, but the GenBank sequence starts and
ends with `GAAC...TATA` and the Forsburg lab sequence with `ACGC...TAGA`.

The two screenshots below show that the cdSEGUID checksums are identical, which proves that the two sequences describe the same double
stranded circular DNA molecule.

#### Genbank sequence for `pFA6a-GFPS65T-kanMX6`

![Genbank](images/genbank.png "GenBank")

#### Forsburg lab sequence for `pFA6a-GFPS65T-kanMX6`

![Forsburg](images/forsburg.png "seguid_calculator")


## Availability

Seguid-calculator is hosted [here](http://seguidcalculator.pythonanywhere.com/)

The online version was built with [flask](https://github.com/pallets/flask) and hosted
on [pythonanywhere](https://www.pythonanywhere.com/).


## lsSEGUID
![](images/slDNA.png)

The **l**inear **s**ingle-strand  SEGUID or **lsSEGUID** is meant for single stranded DNA
or protein sequence which share basic topology, i.e. The sequence has a beginning and an end and only one strand.

lsSEGUID is fundamentally a [base64url](https://en.wikipedia.org/wiki/Base64#URL_applications) encoded version
of the original SEGUID checksum where forward slash and plus (`/` , `+`) characters of  the
standard base64 encoding are replaced by `-` and `_`.
This makes the checksum directly useful as a part of a URL.

## csSEGUID
![](images/scDNA.png)

The **c**ircular **s**ingle-strand  SEGUID or **csSEGUID** is useful for single-stranded circular DNA sequences and other
molecules sharing the same properties. A circular sequence of this type has no identifiable beginning or end and also no
complementary strand. A real world example of this kind of molecule is the M13 phage that maintains its genome as a circular
single stranded molecule.

As there are many permutations of a circular sequence, using the lsSEGUID checksum directly would be impractical as
there could be several checksums for the same sequence. The csSEGUID algorithm first finds
the [lexicographically minimal string rotation](http://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation)
and then applies the same checksum algorithm as for the lsSEGUID.

**N.B.** Plasmids are usually **not** this kind of molecule, see **cdSEGUID** below.


## ldSEGUID
![](images/dlDNA-blunt.png)

The **l**inear **d**ouble-strand  SEGUID or **ldSEGUID** is useful for double-stranded DNA sequences as the one depicted below.
The two representations are equivalent representations of the same DNA molecule.
```
            5'-GATTACA-3'
               |||||||
            3'-CTAATGT-5'

            5'-TGTAATC-3'
               |||||||
            3'-ACATTAG-5'
```

The molecule is made up of two antiparalell complementary strands and has a beginning and an end.
As the strands are complementary, each strand completely identify the other strand in the case of a blunt molecule as the one depicted.

For this reason, most databases only store one of the strands as the other one is easy to infer.
The ldSEGUID algorithm compares two top strands `GATTACA` and `TGTAATC` and chooses the smallest one i.e. (`GATTACA`).

A string, `GATTACA` concatenated with a semicolon `;` character and complementary strand which in most cases is the
reverse complement `GATTACA;CTAATGT` and further processed as for the lsSEGUID checksum.

## cdSEGUID
![](images/dcDNA.png)

The cdSEGUID (**c**ircular **d**ouble-strand SEGUID) checksum is defined for circular dsDNA molecules such as
most [plasmids](http://en.wikipedia.org/wiki/Plasmid) and bacterial chromosomes.

The smallest rotation is found for each of the two strands in a manner similar to that of the csSEGUID checksum.
A string in uppercase letters is constructed from the watson sequence starting at its minimum point, a line break
and the complementary sequence. Another string is constructed from the crick sequence at its minimum point a line
break and a the watson string in 5'-3' order. The two strings are compared and the checksum is calculated from the
string.

### How to install on pythonanywhere:
```
16:33 ~ $ mkvirtualenv --python=python3.9 MyVirtualenv
created virtual environment CPython3.9.5.final.0-64 in 13108ms
  creator CPython3Posix(dest=/home/seguidcalculator/.virtualenvs/MyVirtualenv, clear=False, no_vcs_ignore=False, global
=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/seguidca
lculator/.local/share/virtualenv)
    added seed packages: pip==21.3, setuptools==58.2.0, wheel==0.37.0
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
virtualenvwrapper.user_scripts creating /home/seguidcalculator/.virtualenvs/MyVirtualenv/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/seguidcalculator/.virtualenvs/MyVirtualenv/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/seguidcalculator/.virtualenvs/MyVirtualenv/bin/preactivate
virtualenvwrapper.user_scripts creating /home/seguidcalculator/.virtualenvs/MyVirtualenv/bin/postactivate
virtualenvwrapper.user_scripts creating /home/seguidcalculator/.virtualenvs/MyVirtualenv/bin/get_env_details
(MyVirtualenv) 16:36 ~ $ pip install flask flask-wtf wtforms
Looking in links: /usr/share/pip-wheels
Collecting flask
  Downloading Flask-2.2.2-py3-none-any.whl (101 kB)
     |████████████████████████████████| 101 kB 2.1 MB/s
Collecting flask-wtf
(MyVirtualenv) 16:37 ~ $
(MyVirtualenv) 16:40 ~ $ git checkout https://github.com/BjornFJohansson/seguid_calculator.git
fatal: not a git repository (or any parent up to mount point /home)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
(MyVirtualenv) 16:43 ~ $ git clone https://github.com/BjornFJohansson/seguid_calculator.git
Cloning into 'seguid_calculator'...
remote: Enumerating objects: 1555, done.
remote: Counting objects: 100% (441/441), done.
remote: Compressing objects: 100% (159/159), done.
remote: Total 1555 (delta 236), reused 437 (delta 232), pack-reused 1114
Receiving objects: 100% (1555/1555), 76.46 MiB | 53.41 MiB/s, done.
Resolving deltas: 100% (879/879), done.
Updating files: 100% (48/48), done.
(MyVirtualenv) 16:44 ~ $ ls
README.txt  seguid_calculator
(MyVirtualenv) 16:44 ~ $
```


![](images/pyany_setting1.png)


![](images/pyany_settings2.png)
