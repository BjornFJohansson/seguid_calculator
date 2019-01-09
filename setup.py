#!/usr/bin/env python
# -*- coding: utf-8 -*-

for line in open('seguid_calculator.py'):
    if line.startswith('__'):
        exec(line.strip())

from setuptools import setup

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
        long_description=open('README.md').read(),
        install_requires =["wxpython"],
        zip_safe = False,
        keywords = "bioinformatics",
        classifiers = ['Development Status :: 4 - Beta',
                       'Environment :: Console',
                       'Intended Audience :: Education',
                       'Intended Audience :: Science/Research',
                       'License :: OSI Approved :: BSD License',
                       'Programming Language :: Python :: 2.7',
                       'Topic :: Education',
                       'Topic :: Scientific/Engineering :: Bio-Informatics',])
