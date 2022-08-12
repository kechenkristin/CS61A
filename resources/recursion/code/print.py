# Printing in Recursive Functions
def is_even(n):
    return n % 2 == 0

def cascade(n):
    """
    Print a cascade of prefix of n
    >>> cascade(2013)
    2013
    201
    20
    2
    20
    201
    2013
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)


def cascade1(n):
    """ Print a cascade of prefix of n."""
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)


def inverse_cascade(n):
    """Function that prints an inverse cascade."""
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

def grow(n):
    if n // 10 == 0:
        return
    else:
        grow(n // 10)
        print(n // 10)

def shrink(n):
    if n // 10 == 0:
        return
    else:
        print(n // 10)
        shrink(n // 10)