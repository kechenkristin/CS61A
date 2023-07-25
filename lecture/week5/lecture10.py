"""Function that takes as input integer "n" and returns the sum of the first 'n'
sum(5) returns 1+2+3+4+5 """
def sum_iter(n):
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
