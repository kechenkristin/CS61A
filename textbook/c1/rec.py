def rec(x, y):
    """
    calculate x ** y
    >>> rec(2, 3)
    8
    """
    if y == 0:
        return 1
    else:
        return x * rec(x, y - 1)
