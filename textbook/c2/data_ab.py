from fractions import gcd
"""Data Abstraction."""

def rational(n,d):
    """ Returns the rational number with numerator n and denominator d.
    Represent a rational number as a pair of two integers: a numerator 
    and a denominator."""
    return [n,d]

def lowest_rational(n,d):
    """Reduce the numerator and the denominator to lowest term."""
    g = gcd(n,d)
    return (n//g, d//g)

def numer(x):
    """ Returns the numerator of the rational number x."""
    return x[0]

def denom(x):
    """Returns the denominator of the number x."""
    return x[1]

"""Rational Data Abstraction Implemented as Functions."""
def rational_fun(n,d):
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer_fun(x):
    return x('n')

def denom_fun(x):
    return x('d')

def add_rationals(x,y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rational_are_equal(x,y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def square_rational(x):
    return mul_rational(x,x)

def pair(x, y):
    """Alternative way of creating pair using two functions.Return a function that represents a pair."""
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p,i):
    """Return the element at index i of pair p."""
    return p(i)
