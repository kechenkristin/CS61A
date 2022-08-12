def min_abs_indices(s):
    """ Indices of all elements in list s that has the smallest absolute value.
    >>> min_abs_indices([-4, -3, -2, 3, 2,5])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]
    """
    >>> f = lambda i: abs(s[i]) == min_abs
    >>> list(filter(f, range(len(s))))
    """

def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list.
    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    return max([s[i] + s[i + 1] for i in range(len(s) - 1)])
    """
    max([a + b for a,b in zip(s[:-1], s[1:])])
    """

def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.
    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}


def all_have_an_equal(s):
    """Doea every element equal some other lement in s?
    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    return all([s[i] in s[:i] + s[i + 1:] for i in range(len(s))])
