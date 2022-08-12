# Mutual Recursion
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)


def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)


def iss_even(n):
    if n == 0:
        return True
    else:
        if (n - 1) == 0:
            return False
        else:
            return iss_even((n - 1) - 1)


def play_alice(n):
    """
    Alice always removes a single pebble
    Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise
    """
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n - 1)


def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        play_alice(n - 2)
    else:
        play_alice(n - 1)


def split(n):
    """ Split a positive integer into all but its last digit and remaing part."""
    return n // 10, n % 10


def sum_digits(n):
    """
    Return the sum of the digits of positive integer n.

    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def sum_digits1(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits1(n, digit_sum + last)


# luhn algorithm: mutual recursion

def luhn_sum(n):
    """
    Return the digit sum of n computed by the Luhn algorithm.

    >>> luhn_sum(2)
    2
    >>> luhn_sum(12)
    4
    >>> luhn_sum(42)
    10
    >>> luhn_sum(138743)
    30
    """

    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    """ return the luhn sum of n, doubling the last digit."""
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)

    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
