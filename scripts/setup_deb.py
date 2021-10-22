#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring."""

# build-essential:native python3-setuptools python3-all debhelper

from setuptools import setup
from setuptools import find_packages
from os import path

__author__ = "__author__"
__email__ = "__email__"

for line in open("src/seguid_calculator/calculator.py"):
    if line.startswith("__author__") or line.startswith("__email__"):
        exec(line.strip())

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(  name='seguid_calculator',
		author          =__author__,
		author_email    =__email__,
		packages=find_packages("src"),
		package_dir={"": "src"},
		url='https://github.com/BjornFJohansson/seguid_calculator#seguid_calculator',
		license='LICENSE.txt',
		description='''Calculates SEGUID, cSEGUID & lSEGUID checksums for biological sequences''',
		long_description=open('deb_description.txt').read(),
		setup_requires=["setuptools_scm"],
		install_requires =["wxpython"],
		use_scm_version={"write_to": "src/seguid_calculator/_version.py"},
		entry_points = { 'gui_scripts': ['seguid_calculator = seguid_calculator.calculator:main']},
		keywords = "bioinformatics",
        zip_safe = False,
		classifiers = ['Development Status :: 4 - Beta',
				     'Environment :: Console',
				     'Intended Audience :: Education',
				     'Intended Audience :: Science/Research',
				     'License :: OSI Approved :: BSD License',
				     'Programming Language :: Python :: 3.7',
				     'Programming Language :: Python :: 3.8',
				     'Programming Language :: Python :: 3.9',
				     'Topic :: Education',
				     'Topic :: Scientific/Engineering :: Bio-Informatics'])
