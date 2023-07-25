def make_withdraw(balance):
    """
    >>> wd = make_withdraw(12)
    >>> wd2 = wd
    >>> wd2(1)
    11
    >>> wd(1)
    10
    """

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
            balance = balance = amount
            return balance
        return withdraw


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    "*** YOUR CODE HERE ***"
    a, b = -1, 1

    def fib():
        nonlocal a, b
        a, b = b, a + b
        return b
    return fib


def f(x):
    """
    >>> a = f(1)
    >>> b = a(2)
    >>> b(3) + b(4)
    22
    """
    x = 4

    def g(y):
        def h(z):
            nonlocal x
            x += 1
            return x + y + z
        return h
    return g
