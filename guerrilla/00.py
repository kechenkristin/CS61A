def count_digits(n):
    k = 0
    for x in str(n):
        k += 1
    return k


def count_matches(n,m):
    i, count = 0, 0
    n, m = str(n), str(m)
    for x in n:
        if n[i] == m[i]:
            count += 1
        i += 1
    return count


def make_skipper(n):
    def mutiple_of_num(num):
        if num % n == 0:
            return True
        else:
            return False

    def skipper(m):
        k = 1
        while k <= m:
            if not mutiple_of_num(k):
                print(k)
            k += 1
    return skipper

    
def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 != 0

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true."""
    k = 1
    while k <= n: 
        if cond(k):
            print(k)
        k += 1


def make_keeper(n):
    """ Return a function which takes one parameter cond and prints out all 
    integers 1..i..n where calling cond(i) return True"""

    def cond_func(cond):
        k = 1
        while k <= n:
            if cond(k):
                print(k)
            k += 1
    return cond_func


