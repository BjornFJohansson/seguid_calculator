#!/usr/bin/env python
# -*- coding: utf-8 -*-

for line in open('seguid_calculator.py'):
    if line.startswith('__'):
        exec(line.strip())

from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(  name='seguid_calculator',
        version=__version__,
        author          =__author__,
        author_email    =__email__,
        py_modules=['seguid_calculator'],
        scripts=['seguid_calculator.py'],
        entry_points = { 'gui_scripts': [ 'seguid_calculator = seguid_calculator:main' ]},
        url='http://pypi.python.org/pypi/seguid_calculator',
        license='LICENSE.txt',
        description='''Calculates seguid, lseguid & cseguid checksums for biological sequences''',
        long_description=long_description,
        long_description_content_type='text/markdown',
        install_requires =["wxpython"],
        zip_safe = False,
        keywords = "bioinformatics",
        classifiers = ['Development Status :: 4 - Beta',
                       'Environment :: Console',
                       'Intended Audience :: Education',
                       'Intended Audience :: Science/Research',
                       'License :: OSI Approved :: BSD License',
                       'Programming Language :: Python :: 3.6',
                       'Programming Language :: Python :: 3.7',
                       'Topic :: Education',
                       'Topic :: Scientific/Engineering :: Bio-Informatics',])
