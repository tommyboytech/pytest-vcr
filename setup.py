#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import codecs
from setuptools import setup

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


def install_requires():
    reqs = ['pytest>=3.6.0', 'vcrpy']
    if PY2:
        reqs.append('gevent==1.2.2')
    if PY3:
        reqs.append('gevent==1.5.0')


setup(
    name='pytest-vcr',
    version='1.0.2',
    author='Tomasz Kontusz',
    author_email='tomasz.kontusz@gmail.com',
    maintainer='Tomasz Kontusz',
    maintainer_email='tomasz.kontusz@gmail.com',
    license='MIT',
    url='https://github.com/ktosiek/pytest-vcr',
    description='Plugin for managing VCR.py cassettes',
    long_description=read('README.rst'),
    py_modules=['pytest_vcr'],
    install_requires=install_requires(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'vcr = pytest_vcr',
        ],
    },
)
