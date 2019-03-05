#!/usr/bin/python3

import os
import sys
import re
from setuptools import setup
from SAGA_optimize import __version__


setup(
    name='SAGA_optimize',
    version=__version__,
    author='Huan Jin',
    author_email='hji236@g.uky.edu',
    description='Optimization method for solving boundary-value inverse problem based on a combined simulated annealing and genetic algorithm',
    keywords="optimization inverse problem simulated annealing genetic algorithm",
    license='BSD',
    url='https://hji236@gitlab.cesb.uky.edu/hji236/SAGA_optimize.git',
    py_modules=['SAGA_optimize'],
    install_requires=['jsonpickle'],
    platforms='any',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

    ]


)