# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import simple_search
version = simple_search.__version__

setup(
    name='Simple Search',
    version=version,
    author='',
    author_email='simple@email.com',
    packages=[
        'simple_search',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['simple_search/manage.py'],
)