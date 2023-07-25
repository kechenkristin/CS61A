from operator import add, mul, truediv

def divide_all(n, ds):
    """
    >>> divide_all(1024, [2, 4, 0, 8])
    inf
    >>> divide_all(1024, [2, 4, 8])
    16.0
    """
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

def devide_all(n, ds):
    """Combine elements of s using f start with initial.

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial


def reduce_rec(f, s, initial):
    if not s:
        return initail
    else:
        first, rest = s[0], s[1:]
        return reduce_rec(f, rest, f(initial, first))
