def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def count(f):
    """
    >>> fib = count(fib)
    >>> fib(5)
    5
    >>> fib.call_count
    15
    """
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted


def memo(f):
    """
    >>> fib = memo(fib)
    >>> fib(5)
    5
    >>> fib.call_count 
    6
    """
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
