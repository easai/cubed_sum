import random

from cubed_sum.cubed_sum import cubed_sum, Parity
from cubed_sum.cubed_sum_naive import naive_cubed_sum, naive_cubed_sum_even, naive_cubed_sum_odd


def test_negative():
    a = -5
    b = 5
    assert cubed_sum(a, b) == naive_cubed_sum(a, b)


def test_negative_even():
    a = -5
    b = 5
    assert cubed_sum(a, b, Parity.EVEN) == naive_cubed_sum_even(a, b)


def test_negative_odd():
    a = -5
    b = 5
    assert cubed_sum(a, b, Parity.ODD) == naive_cubed_sum_odd(a, b)


def test_oddeven():
    a = 1
    b = 4
    assert cubed_sum(a, b) == naive_cubed_sum(a, b)


def test_oddeven_even():
    a = 1
    b = 4
    assert cubed_sum(a, b, Parity.EVEN) == naive_cubed_sum_even(a, b)


def test_oddeven_odd():
    a = 1
    b = 4
    assert cubed_sum(a, b, Parity.ODD) == naive_cubed_sum_odd(a, b)


def test_evenodd():
    a = 2
    b = 5
    assert cubed_sum(a, b) == naive_cubed_sum(a, b)


def test_evenodd_even():
    a = 2
    b = 5
    assert cubed_sum(a, b, Parity.EVEN) == naive_cubed_sum_even(a, b)


def test_evenodd_odd():
    a = 2
    b = 5
    assert cubed_sum(a, b, Parity.ODD) == naive_cubed_sum_odd(a, b)


def test_random():
    a = random.randint(-10**6, -10**3)  # Random large negative integer
    b = random.randint(10**3, 10**6)    # Random large positive integer
    assert cubed_sum(a, b) == naive_cubed_sum(a, b)


def test_random_even():
    a = random.randint(-10**6, -10**3)
    b = random.randint(10**3, 10**6)
    assert cubed_sum(a, b, Parity.EVEN) == naive_cubed_sum_even(a, b)


def test_random_odd():
    a = random.randint(-10**6, -10**3)
    b = random.randint(10**3, 10**6)
    assert cubed_sum(a, b, Parity.ODD) == naive_cubed_sum_odd(a, b)
