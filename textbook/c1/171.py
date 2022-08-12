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
