""" Our first Python source file"""

from operator import floordiv, mod

def divide_exact(n, d= 10):
    """ Return the quotient and reminder of dividing n by d."""
    return floordiv(n,d),mod(n,d)

def absolute_value(x):
    """ Return the absolute value of x."""
    if x < 0:
        return -x
    elif x==0:
        return 0
    else: 
        return x
