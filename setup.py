#!/usr/bin/env python3
"""golflang-encodings: a bunch of codecs for various esoteric programming languages"""

from setuptools import setup, find_packages

setup(
    name='golflang-encodings',

    version='1.0.2',

    description='a bunch of codecs for various esoteric programming languages',

    url='https://github.com/PPCG-v2/golflang-encodings',
    
    packages=find_packages(),

    author='Mego',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='text encoding unicode',
)
