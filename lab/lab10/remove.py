def remove(item, lst):
    """ takes in a list and returns a new list with all instances of item removed from lst.
    >>> remove(3, [1, 3, 5])
    [1, 5]
    >>> remove(5, [5, 3, 5, 5, 1, 4, 5, 4])
    [3, 1, 4, 4]
    """
    if len(lst) == 0:
        return []
    elif lst[0] == item:
        return remove(item,lst[1:])
    else:
        remain = [lst[0]]
        return remain + remove(item, lst[1:])
