"""
Tests for stats functions
"""
import random
from stats import *


def approx(a, b, epsilon=1e-6):
    return abs(a-b) < epsilon


def test_find_bin():

    # one big bin for all real numbers
    assert find_bin(123, []) == 0

    # divide into + and -
    assert find_bin(123, [0]) == 1
    assert find_bin(0.0, [0]) == 1
    assert find_bin(0, [0]) == 1
    assert find_bin(0.00001, [0]) == 1
    assert find_bin(-0.00001, [0]) == 0
    assert find_bin(-1, [0]) == 0
    assert find_bin(-123, [0]) == 0

    deciles = list(range(10,100,10))
    assert find_bin(5, deciles) == 0
    assert find_bin(15, deciles) == 1
    assert find_bin(95, deciles) == 9
    assert find_bin(105, deciles) == 9


def test_hist():
    deciles = list(range(10,100,10))
    grades = [75,87,88,92,93,84,96,99,79,100,98]
    h = hist(grades, deciles)
    assert h[0] == 0
    assert h[1] == 0
    assert h[7] == 2
    assert h[8] == 3
    assert h[9] == 6


def test_mean():
    assert mean([1,2,3,4,5,6,7,8,954,10]) == 100.0


def test_median():
    assert median([1,2,3,4,5,6,7,8,954,10]) == 5.5
    assert median([1,2,3,4,5,6,7,8,954]) == 5
    assert median([1,2,999]) == 2
    assert median([1,999]) == 500

def test_sd():
    assert approx(standard_deviation([1,2]), 0.7071068)
    assert approx(standard_deviation([1,2,3,4,5,6,7]), 2.160247)
    assert approx(
        standard_deviation([random.gauss(0,1) for _ in range(1000)]), 1.0,
        epsilon=0.3)
