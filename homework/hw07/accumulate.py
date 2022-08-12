from operator import mul, add, sub

def accumulate(combiner, start, n, term):
    """
    combiner: a function of two arguments
    start: a number with which to start combining
    n: the number of natural numbers to combine
    term: a function of one argument that cpmputes the nth term of a sequence.
    
    >>> accumulate(mul, 1, 5, identity) # 1 * 1 * 2 * 3 * 4 * 5
    120
    >>> accumulate(add, 0, 5, square)   # 0 + 1^2 + 2^2 + 3^2 + 4^2 + 5^2
    55
    >>> accumulate(add, 5, 5, square)   # 5 + 1^2 + 2^2 + 3^2 + 4^2 + 5^2
    60
    """
    result = start
    for i in range(1, n + 1):
        result = combiner(result, term(i))
    return result


def accumulate_rec(combiner, start, n, term):
    """ 
    >>> accumulate_rec(mul, 1, 5, identity)
    120
    >>> accumulate_rec(add, 0, 5, square)
    55
    >>> accumulate_rec(add, 5, 5, square)
    60
    """
    if n == 0:
        return start
    else:
        return combiner(term(n), accumulate_rec(combiner, start, n - 1, term))


def identity(x):
    return x

def square(x):
    return x * x
