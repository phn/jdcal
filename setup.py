#!/usr/bin/env python

from distutils.core import setup

import jdcal

version = jdcal.__version__

setup(
    name="jdcal",
    version=version,
    description="Julian dates from proleptic Gregorian and Julian calendars.",
    license='BSD',
    author="Prasanth Nair",
    author_email="prasanthhn@gmail.com",
    url='https://github.com/phn/jdcal',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Programming Language :: Python',
        ],
    py_modules=["jdcal"]
    )
