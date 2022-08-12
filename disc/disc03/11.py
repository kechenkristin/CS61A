def mutiply(m,n):
    """ A function takes two numbers and returns their product, using recursion"""
    if m < n:
        m,n = n,m
    if n == 1:
        return 0
    else:
        digit = n - 1
        result = m * digit
        return mutiply(m,digit) + result 
