def square(x):
    return x * x

def is_odd(x):
    return x % 2 == 1


def pow(x, y):
    """ Raising the number x to the power of a nonnegative integer y for which 
    the number of operations grows logarithmically.
    >>> pow(2, 5)
    32
    >>> pow(3, 3)
    27
    >>> pow(8, 2)
    64
    >>> pow(1, 222)
    1
    """
    if x == 1:
        return 1
    elif y == 1:
        return x
    elif is_odd(y):
        return x * square(pow(x, (y - 1) // 2))
    else:
        return square(pow(x, y // 2))
