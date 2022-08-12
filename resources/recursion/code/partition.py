# Partitions
def count_partitions(n, m):
    """
    Count the ways to partition n using parts up to m.
    6 = 2 + 4
    6 = 1 + 1 + 4
    6 = 3 + 3
    6 = 1 + 2 + 3
    6 = 1 + 1 + 1 + 3
    6 = 2 + 2 + 2
    6 = 1 + 1 + 2 + 2
    6 = 1 + 1 + 1 + 1 + 2
    6 = 1 + 1 + 1 + 1 + 1 + 1
    >>> count_partitions(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m


def next_largest_coin(coin):
    """Return the next coin.
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                           
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(lowest, n):
        if lowest == None:
            return 0

        elif lowest == n:
            return 1

        elif lowest > n:
            return 0

        with_coin = helper(lowest, n - lowest)
        without_coin = helper(next_largest_coin(lowest), n)
        return with_coin + without_coin
    return helper(1, total)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1:
        return 1
    elif n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)
