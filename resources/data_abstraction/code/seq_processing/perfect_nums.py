from operator import add
from functools import *


def divisors(n):
    """
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]


def perfect_nums(max_range):
    """
    Return perfect numbers within the max_range.
    >>> perfect_nums(1000)
    [6, 28, 496]
    """
    return [n for n in range(1, max_range) if sum(divisors(n)) == n]


# find perfect number using these higher-order functions


def divisors_of(n):
    def divides_n(x): return n % x == 0
    return [1] + keep_if(divides_n, range(2, n))


def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)


def perfect(n):
    return sum_of_divisors(n) == n
