"""Goal: one more multiplication lets us double the problem size."""

def exp_std(b,n):
    """ Based on definition of exponentiation, calculate b**n."""
    if n == 0:
        return 1
    else:
        return b * exp_std(b, n - 1)


def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n // 2))
    else:
        return b * exp_fast(b, n - 1)


def square(x):
    return x * x
