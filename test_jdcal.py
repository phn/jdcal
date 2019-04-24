"""Tests for jdcal.py"""
import pytest

from jdcal import (
    ipart, is_leap, gcal2jd, jd2gcal, jcal2jd, jd2jcal, MJD_0)


def test_ipart():
    assert round(ipart(20.345), 12) == 20.0
    assert round(ipart(-20.345), 12) == -20.0
    assert round(ipart(0.12345), 12) == -0.0
    assert round(ipart(-0.6789), 12) == -0.0


def test_is_leap():
    assert is_leap(2000)
    assert not is_leap(2001)
    assert is_leap(2004)
    assert not is_leap(1000)
    assert not is_leap(1998)
    assert is_leap(1992)


def test_gcal2jd_simple():
    r = gcal2jd(2000, 1, 1)
    assert round(r[0], 12) == 2400000.5
    assert round(r[1], 12) == 51544.0


def test_gcal2jd_negative_numbers_and_zero():
    assert gcal2jd(2000, -2, -4) == gcal2jd(1999, 9, 26)
    assert gcal2jd(2000, 2, -1) == gcal2jd(2000, 1, 30)
    assert gcal2jd(2000, 3, -1) == gcal2jd(2000, 2, 28)

    assert gcal2jd(2000, 3, 0) == gcal2jd(2000, 2, 29)
    assert gcal2jd(2001, 3, 0) == gcal2jd(2001, 2, 28)


def test_gcal2jd_next_month():
    assert gcal2jd(2000, 2, 30) == gcal2jd(2000, 3, 1)
    assert gcal2jd(2001, 2, 30) == gcal2jd(2001, 3, 2)
    assert gcal2jd(2000, 12, 32) == gcal2jd(2001, 1, 1)


def test_gcal2jd_is_for_mid_night_of_given_day():
    # input values are truncated to integers. So this is trivial.
    assert gcal2jd(1996, 4, 3) == gcal2jd(1996, 4, 3.5)
    assert gcal2jd(2000, 10, 25) == gcal2jd(2000, 10, 25.9)


def test_jd2gcal():
    assert jd2gcal(*gcal2jd(2000, 1, 1)) == (2000, 1, 1, 0.0)
    assert jd2gcal(*gcal2jd(1950, 1, 1)) == (1950, 1, 1, 0.0)
    assert jd2gcal(*gcal2jd(1999, 10, 12)) == (1999, 10, 12, 0.0)
    assert jd2gcal(*gcal2jd(2000, 2, 30)) == (2000, 3, 1, 0.0)
    assert jd2gcal(*gcal2jd(2000, -2, -4)) == (1999, 9, 26, 0.0)


def test_jd2gcal_fractional_day_part():
    r = jd2gcal(2400000.5, 51544.0 + 0.5)
    assert round(r[-1], 12) == 0.5

    r = jd2gcal(2400000.5, 51544.0 + 0.245)
    assert round(r[-1], 10) == round(0.245, 10)

    r = jd2gcal(2400000.5, 51544.0 + 0.75)
    assert round(r[-1], 12) == 0.75


def test_jcal2jd_and_back_through_jd2jcal():
    """Check round trip from jcal2jd to jd2jcal."""
    import random
    n = 1000
    year = [random.randint(-4699, 2200) for i in range(n)]
    month = [random.randint(1, 12) for i in range(n)]
    day = [random.randint(1, 28) for i in range(n)]

    jd = [jcal2jd(y, m, d)[1]
          for y, m, d in zip(year, month, day)]

    x = [jd2jcal(MJD_0, i) for i in jd]

    for i in range(n):
        assert x[i][0] == year[i]
        assert x[i][1] == month[i]
        assert x[i][2] == day[i]
        assert x[i][3] <= 1e-15


def astropy_erfa_un_available():
    x = True
    try:
        from astropy import _erfa
        import numpy as np
        _erfa.cal2jd
        np.allclose
        x = False
    except:
        pass
    return x


@pytest.mark.skipif(astropy_erfa_un_available(), reason="astropy._erfa not available")
def test_gcal2jd_with_astropy_erfa_cal2jd():
    """Compare gcal2jd with astropy._erfa.cal2jd."""
    import random
    import numpy as np
    from astropy import _erfa

    n = 1000
    mday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # sla_cldj needs year > -4699 i.e., 4700 BC.
    year = [random.randint(-4699, 2200) for i in range(n)]
    month = [random.randint(1, 12) for i in range(n)]
    day = [random.randint(1, 31) for i in range(n)]
    for i in range(n):
        x = 0
        if is_leap(year[i]) and month[i] == 2:
            x = 1
        if day[i] > mday[month[i]] + x:
            day[i] = mday[month[i]]

    jd_jdcal = np.array([gcal2jd(y, m, d) for y, m, d in zip(year, month, day)])
    jd_erfa = np.array(_erfa.cal2jd(year, month, day)).T

    assert np.allclose(jd_jdcal, jd_erfa)
