"""Generalization."""

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n,term):
    """Sum the first N terms of a sequence.

    >>> summation(10, square)
    385
    """

    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k+1
    return total

def sum_naturals(n):
    """
    >>> sum_naturals(10)
    55
    """
    return summation(n,identity)

def sum_cubes(n):
    return summation(n,cube)


def pi_term(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))


def pi_sum(n):
    return summation(n, pi_term)

def make_adder(n):
    """
    >>> add1 = make_adder(1)
    >>> add1(2)
    3
    """
    
    def adder(k):
        return k + n
    return adder