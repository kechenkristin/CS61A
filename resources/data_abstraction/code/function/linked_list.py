""" Linked List"""

empty = 'empty'


def is_link(s):
    """ s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """
    Construct a linked list from its first element and the rest.

    >>> four = link(1, link(2, link(3, link(4, empty))))
    [1, [2, [3, [4, 'empty']]]]
    """
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]


def first(s):
    """ Return the first element of a linked list s."""
    assert is_link(s), " first only applies ti linked list."
    assert s != empty, "empty list has no first element."
    return s[0]


def rest(s):
    """
    Return the rest of the element of a linked list s.

    >>> rest(four)
    [2, [3, [4, 'empty']]]
    """
    assert is_link(s), "rest only applies to linked list."
    assert s != empty, "empty linkd list has no rest."
    return s[1]


def len_link(s):
    """ 
    Return the length of linked list s.

    >>> len_link(four)
    4
    """
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def len_link_recursive(s):
    """ Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))


def getitem_link(s, i):
    """ Return the element at index i of linked list s.

    >>> getitem_link(four, 1)
    2
    """
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


def getitem_link_recursive(s, i):
    if i == 0:
        return first(s)
    else:
        return getitem_link_recursive(rest(s), i - 1)


def extend_link(s, t):
    """ Return a list with the element of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))


def apply_to_all_link(f, s):
    """Apply f to each element of s.

    >>> apply_to_all_link(lambda x: x*x, four)
    [1, [4, [9, [16, 'empty']]]]
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


def keep_if_link(f, s):
    """
    Return a list with element of s for which f(e) is true.

    >>> kept_if_link(lambda x: x%2 == 0, four)
    [2, [4, 'empty']]
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept


def join_link(s, separator):
    """ Return a string of all elements in s separated by peparator.
    >>> join_link(four, ", ")
    '1, 2, 3, 4'
    """
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
