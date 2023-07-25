"""Higher Order Functions"""
def apply_to_all(map_fn, s):
    """Evaluating an expression for each element in a sequence can be expressed by
    applying a function to each element."""
    return [map_fn(x) for x in s]

apply_to_all_lam = lambda map_fn, s: list(map(map_fn, s))


def keep_if(filter_fn, s):
    """Selecting element for which some expression is true can be expressed
    by applying a function to each element."""
    return [x for x in s if filter_fn(x)]

keep_if_lam = lambda filter_fn, s: list(filter(filter_fn, s))


def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced,x)
    return reduced
