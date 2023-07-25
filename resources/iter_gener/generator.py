""" A yield from statement yields all values from an iterator or iterable."""


def even(start, end):
    """
    A generator function that returns even numbers

    >>> list(even(2, 10))
    [2, 4, 6, 8]
    >>> list(even(1, 10))
    [2, 4, 6, 8]
    """
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


def a_then_b1(a, b):
    """
    >>> list(a_then_b([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    for x in a:
        yield x
    for x in b:
        yield x


def a_then_b(a, b):
    yield from a
    yield from b


def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)


def prefixes(s):
    """
    yields all prefixes of s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """

    if s:
        yield from prefixes(s[:-1])
        yield s


def substrings(s):
    """
    yields all substrings of s.

    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])


def merge(a, b):
    """
    >>> def sequence(start, step):
    ... while True:
    ... yield start
    ... start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """

    first_a, first_b = next(a), next(b)
    while True:
        if first_a == first_b:
            yield first_a
            first_a, first_b = next(a), next(b)
        elif first_a < first_b:
            yield first_a
            first_a = next(a)
        else:
            yield first_b
            first_b = next(b)


def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ... print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """

    subset = [[]]
    n = 1
    while True:
        yield subset
        subset += [s + [n] for s in subset]
