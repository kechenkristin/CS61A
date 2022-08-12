def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total

def pi_sum(n):
    total, k = 0,1
    while k <= n:
        total, k = total + 8/((4*k-3) * (4*k-1)), k + 1
    return total

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n,cube)

print("sum of 1*1*1 + 2*2*2 + 3*3*3 :",sum_cubes(3))
