import math

def is_prime(n):
    i = 2
    flag = True
    while i < math.sqrt(n):
        if n % i == 0:
            flag = False
            return flag
        i += 1
    return flag




