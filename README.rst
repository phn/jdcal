jdcal
=====

.. _TPM: http://www.sal.wisc.edu/~jwp/astro/tpm/tpm.html
.. _Jeffrey W. Percival: http://www.sal.wisc.edu/~jwp/
.. _IAU SOFA: http://www.iausofa.org/
.. _pip: http://pypi.python.org/pypi/pip
.. _easy_install: packages.python.org/distribute/easy_install.html

This module contains functions for converting between Julian dates and
calendar dates.

A function for converting Gregorian calendar dates to Julian dates, and
another function for converting Julian calendar dates to Julian dates
are defined. Two functions for the reverse calculations are also
defined.

Different regions of the world switched to Gregorian calendar from
Julian calendar on different dates. Having separate functions for Julian
and Gregorian calendars allow maximum flexibility in choosing the
relevant calendar.

Julian dates are stored in two floating point numbers (double).  Julian
dates, and Modified Julian dates, are large numbers. If only one number
is used, then the precision of the time stored is limited. Using two
numbers, time can be split in a manner that will allow maximum
precision. For example, the first number could be the Julian date for
the beginning of a day and the second number could be the fractional
day. Calculations that need the latter part can now work with maximum
precision.

All the above functions are "proleptic". This means that they work for
dates on which the concerned calendar is not valid. For example,
Gregorian calendar was not used prior to around October 1582.

A function to test if a given Gregorian calendar year is a leap year is
also defined.

Zero point of Modified Julian Date (MJD) and the MJD of 2000/1/1
12:00:00 are also given as module level constants.

This module is based on the `TPM`_ C library, by `Jeffrey
W. Percival`_. The idea of splitting Julian date into two floating
point numbers was inspired by the `IAU SOFA`_ C library.

Installation
------------

The module can be installed using `pip`_ or `easy_install`_::

  $ pip install jdcal

or,

::

  $ easy_install jdcal


Credits
--------

1. A good amount of the code is based on the excellent `TPM`_ C library
   by `Jeffrey W. Percival`_. A Python interface to this C library is
   available at http://github.com/phn/pytpm.
2. The inspiration to split Julian dates into two numbers came from the
   `IAU SOFA`_ C library. No code or algorithm from the SOFA library is
   used in `jdcal`.

License
-------

Released under BSD; see
http://www.opensource.org/licenses/bsd-license.php.

For comments and suggestions, email to user `prasanthhn` in the `gmail.com`
domain.

