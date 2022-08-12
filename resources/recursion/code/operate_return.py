# operate return value

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def multiply(m, n):
    """
    5*3 = 5 + 5 + 5
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)


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


def sum_iter(n):
    """
    Function that takes as input integer "n" and returns the sum of the first 'n'
    >>> sum_iter(5) # 5 + 4 + 3 + 2 + 1
    15
    """
    total = 0
    for i in range(0, n+1):
        total += i
    return total


def sum_rec(n):
    if n == 0:
        return 0
    else:
        return n + sum_rec(n - 1)


"""Reverse a string."""


def reverse_iter(s):
    return s[::-1]


def reverse_rec(s):
    if len(s) == 1:
        return s
    else:
        return reverse_rec(s[1::]) + s[0]


def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    """
    lst = list(range(0,n+1))[::-1][::2]
    return reduce(add,lst,0)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + skip_add(n - 2)


def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(1)
    else:
        return summation(n-1, term) + term(n)
