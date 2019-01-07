#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versioneer

for line in open('seguid_calculator/__init__.py'):
    if line.startswith('__') and not line.startswith('__version') and not line.startswith('__long'):
        exec(line.strip())

from setuptools import setup

setup(  name='seguid_calculator',
        version=versioneer.get_version()[:5],
        cmdclass=versioneer.get_cmdclass(),
        author          =__author__,
        author_email    =__email__,
        packages=['seguid_calculator'],
        entry_points = { 'gui_scripts': [ 'seguid_calculator = seguid_calculator.seguid:main' ]},
        url='http://pypi.python.org/pypi/seguid_calculator',
        license='LICENSE.txt',
        description='''Calculates seguid, lseguid & cseguid checksums for biological sequences''',
        long_description=open('README.md').read(),
        install_requires =["wxpython"],
        data_files=[('/usr/share/icons', ['seguid_calculator.png'])],
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
