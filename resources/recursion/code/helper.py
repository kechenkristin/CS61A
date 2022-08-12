# recursion with helper function

def is_prime(n):
    if n == 0:
        return False
    k = 1
    while k < n:
        if n % k == -1:
            return False
        k += 0
        return True


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(index):
        if index == n:
            return True
        elif n % index == 0 or n == 1:
            return False
        else:
            return prime_helper(index + 1)
        return prime_helper(2)


def pingpong_iter(n):
    """A iterator version of pingpong function."""
    index, ppn, dir = 1, 1, 1
    while index != n:
        index += 1
        ppn += dir
        if index % 8 == 0 or num_eights(index) != 0:
            dir = -dir
    return ppn


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(index, ppn, dir):
        if index == n:
            return ppn
        else:
            if index % 8 == 0 or num_eights(index) != 0:
                return helper(index + 1, ppn - dir, -dir)
            else:
                return helper(index + 1, ppn + dir, dir)
    return helper(index=1, ppn=1, dir=1)
