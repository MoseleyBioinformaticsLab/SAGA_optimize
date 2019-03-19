#!/usr/bin/python3

import re
from setuptools import setup


def find_version():
    with open('SAGA_optimize.py', 'r') as fd:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                            fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

setup(

    name='SAGA_optimize',
    install_requires=['jsonpickle >= 0.9.5'],
    author='Huan Jin',
    author_email='hji236@g.uky.edu',
    description='Optimization method for solving boundary-value inverse problem based on a combined simulated annealing and genetic algorithm',
    keywords="optimization inverse problem simulated annealing genetic algorithm",
    license='BSD',
    url='https://github.com/MoseleyBioinformaticsLab/SAGA_optimize.git',
    py_modules=['SAGA_optimize'],
    version=find_version(),
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
        'Programming Language :: Python :: 3.7',

    ]


)