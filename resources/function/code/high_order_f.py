import math

e = math.exp(1)

# function as arguments
# function as general methods


def improve(update, close, guess=1):
    """
    >>> improve(golden_update, square_close_to_successor)
    1.6180339887498951
    """
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    return 1/guess + 1


def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)


def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance


def average(x, y):
    return (x + y)/2

# nested definitions


def sqrt(a):
    """
    >>> sqrt(256)
    16.0
    """
    def sqrt_update(x):
        return average(x, a/x)

    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

# function as returned values


def square(x):
    return x * x


def successor(x):
    return x + 1


def compose1(f, g):
    """
    >>> square_successor = compose1(square, successor)
    >>> result = square_successor(12)
    169
    """
    def h(x):
        return f(g(x))
    return h


"""curring, function takes mutiple arguments into a chain of functions that each take a single argument."""


def curried_pow(x):
    """
    >>> curried_pow(2)(3)
    8
    """

    def h(y):
        return pow(x, y)
    return h


def map_to_range(start, end, f):
    """
    >>> map_to_range(0, 10,curried_pow(2))
    1
    2
    4
    8
    16
    32
    64
    128
    256
    512
    """
    while start < end:
        print(f(start))
        start += 1


def curry2(f):
    """ Return a curried version of the given two-argument function.

    >>> pow_curried = curry2(pow)
    >>> pow_curried(2)(5)
    32
    """

    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def curry2_lam(f):
    return lambda h: lambda x: lambda y: h(x, y)


def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    return lambda x: lambda y: func(x, y)


def uncurry2(g):
    """ Return a two argument version of the given curried function.

    >>> pow_uncurried = uncurry2(pow)
    >>> pow_uncurried(2, 5)
    32
    """
    def f(x, y):
        return g(x)(y)
    return f


def apply_twice(f, x):
    """
    >>> result = apply_twice(square, 2)
    16
    """
    return f(f(x))


def square(x):
    return x*x


def repeat(f, x):
    """
    >>> result = repeat(g, 5)
    2
    """
    while f(x) != x:
        x = f(x)
    return x


def g(y):
    return (y + 5) // 3


def end(n, d):
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None


def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1


def is_three(x):
    return x == 3


def square(x):
    return x * x


def positive(x):
    return max(0, square(x) - 100)


def inverse(f):
    """ Return g(y) such that g(f(x)) -> x.
    >>> sqrt = inverse(square)
    >>> sqrt(256)
    16
    """
    return lambda y: search(lambda x: f(x) == y)


# self reference
def print_all(x):
    """
    >>> print_all(1)(3)(5)
    1
    3
    5
    """
    print(x)
    return print_all


def print_sums(x):
    """
    >>> print_sums(1)(3)(5)
    1
    4
    9
    """
    print(x)

    def next_sum(y):
        return print_sums(x+y)
    return next_sum


def print_delayed(x):
    """Return a new function. This new function, when called,
    will print out x and return another function with the same
    behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> # a function is returned
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print


def count_factors(n):
    """Return the number of positive factors that n has.
    >>> count_factors(6)
    4   # 1, 2, 3, 6
    >>> count_factors(4)
    3   # 1, 2, 4
    """
    i, count = 1, 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)
    3   # 2, 3, 5
    >>> count_primes(13)
    6   # 2, 3, 5, 7, 11, 13
    """
    i, count = 1, 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count


def is_prime(n):
    return count_factors(n) == 2  # only factors are 1 and n


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def helper(n):
        i, count = 0, 0
        while i <= n:
            if condition(i):
                count += 1
            i += 1
        return count
    return helper


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print
