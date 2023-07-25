def fib(n):
    """
    >>> fib(5)
    5
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


def count(f):
    """
    >>> fib = count(fib)
    >>> fib(19)
    4181
    >>> fib.call_count
    13529
    """
        
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted


def count_frames(f):
    """
    >>> fib = count_frames(fib)
    >>> fib(19)
    4181
    >>> fib.open_count
    0
    >>> fib.max_count
    19
    >>> fib(24)
    46368
    >>> fib.max_count
    24
    """

    def counted(*args):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(*args)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted


def memo(f):
    """
    >>> count_fib = count(fib)
    >>> fib = memo(counted_fib)
    >>> fib(19)
    4181
    >>> counted_fib.call_count
    20
    >>> fib(34)
    5702887
    >>> counted_fib.call_count
    35
    """

    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
            return cache[n]
        return memoized
