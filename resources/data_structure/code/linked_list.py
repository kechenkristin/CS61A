class Link:

    # (): Some zero-length sequence
    empty = ()

    def __init__(self, first, rest = empty):
        """
        s = Link(3, Link(4, Link(5)))
        """
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            rest_repr = ''
        else:
            rest_repr = ', ' + repr(self.rest)
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def test_empty(link):
    if link is Link.empty:
        print('This linked list is empty!')
    else:
        print('This linked list is not empty!')


"""Linked list Processing."""
square, odd = lambda x: x * x, lambda x: x % 2 == 1
s = list(map(square, filter(odd, range(1, 6))))     # [1, 9, 25]


def convert_to_lnk(lst):
    """
    Convert a python list to a linked list.

    >>> convert_to_lnk([1, 2, 3, 4])
    Link(1, Link(2, Link(3, Link(4))))
    """
    if len(lst) == 0:
        return Link.empty
    else:
        return Link(lst[0], convert_to_lnk(lst[1:]))


def range_link(start, end):
    """ Return a Link containing consecutive integers from start to end.

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))


def map_link(f, s):
    """ Return a link that contains f(x) for each x in Link s.

    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def deep_map(fn, lst):
    """
    Applies fn to every element in lst.

    >>> normal = Link(1, Link(2, Link(3)))
    >>> deep_map(lambda x: x*x, normal)
    Link(1, Link(4, Link(9)))

    >>> nested = Link(Link(1, Link(2)), Link(3, Link(4)))
    >>> deep_map(lambda x: x * x, nested)
    Link(Link(1, Link(4)), Link(9, Link(16)))
    """
    if lst is Link.empty:
        return lst
    if type(lst.first) == Link:
        deep_map(fn, lst.first)
    else:
        return Link(fn(lst.first), deep_map(fn, lst.rest))
        


def filter_link(f, s):
    """ Return a link that contains only the elements x of link s for which 
        f(x) is a true value.

    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest


def filter_link(link, f):
    """ Takes in a linked list link and a function f and returns gnerator which
    yields the values of link for which f returns True.
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest


def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)

def add(s, v):
    """ Add v to an ordered list s with no repeats, returning modified s.
    If v is already in s, then don't modify s, but still return it.
    """
    assert s is not List.empty
    # add to first
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    # only one element v in linked list
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


def sum_nums(lst):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lst == Link.empty:
        return 0
    return lst.first + sum_nums(lst.rest)


def mutiply_lnks(lst_of_lnks):
    """Takes in a Python list of linked lists and mutiplies them element-wise.
    It should return a new linked list.
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = mutiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rests = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, mutiply_lnks(lst_of_lnks_rests))


def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    new_lst = []
    while link is not Link.empty:
        new_lst.append(link.first)
        link = link.rest
    return new_lst

def convert_link_rec(link):
    """
    >>> link = Link(1,Link(2, Link(3, Link(4))))
    >>> convert_link_rec(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    if link is Link.empty:
        return []
    else:
        return [link.first] + convert_link_rec(link.rest)



def every_other(s):
    """ Takes a linked list s, mutates s such that all of the odd indexed elements
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    cur_link = s
    while cur_link != Link.empty and cur_link.rest != Link.empty:
        cur_link.rest = cur_link.rest.rest
        cur_link = cur_link.rest


def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    """
    seen = []
    cur_link = link
    while cur_link != Link.empty:
        if cur_link in seen:
            return True
        seen.append(cur_link)
        cur_link = cur_link.rest
    return False


def store_digits(n):
    """Store the digits of a positive number n in a linked list

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    if n == 0:
        return Link.empty
    temp = n
    num = 0
    while temp // 10 != 0:
        temp = temp // 10
        num += 1
    return Link(temp, store_digits(n % (10 ** num)))


def store_digits_reverse(n):
    """
    >>> s = store_digits_reverse(2345)
    >>> s
    Link(5, Link(4, Link(3, Link(2))))
    """
    if n == 0:
        return Link.empty
    else:
        return Link(n % 10, store_digits_reverse(n // 10))


def interleave(first, second):
    """
    >>> s1 = Link(1, Link(3, Link(5)))
    >>> s2 = Link(2, Link(4, Link(6)))
    >>> new_lst = interleave(s1, s2)
    >>> new_lst 
    Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    """
    if first is Link.empty:
        return second
    elif second is Link.empty:
        return first
    else:
        if first.first < second.first:
            return Link(first.first, interleave(first.rest, second))
        else:
            return Link(second.first, interleave(first, second.rest))



def remove(lnk, element):
    """ A function takes a linked list and an element and returns a list removing element from lnk.

    >>> s1 = Link(1, Link(2, Link(3, Link(4))))
    >>> remove(s1, 2)
    Link(1, Link(3, Link(4)))
    >>> s2 = Link(5, Link(6, Link(7)))
    >>> remove(s2, 9)
    Link(5, Link(6, Link(7)))
    """
    if lnk is Link.empty:
        return lnk
    elif lnk.first == element:
        lnk = lnk.rest
        return lnk
    else:
        return Link(lnk.first, remove(lnk.rest, element))

def remove2(lnk, element):
    """
    >>> s1 = Link(1, Link(2, Link(3, Link(4))))
    >>> remove2(s1, 2)
    Link(1, Link(3, Link(4)))
    >>> s2 = Link(5, Link(6, Link(7)))
    >>> remove2(s2, 9)
    Link(5, Link(6, Link(7)))
    """
    if lnk is Link.empty:
        return lnk
    elif lnk.first == element:
        return remove2(lnk.rest, element)
    else:
        return Link(lnk.first, remove2(lnk.rest, element))
 
