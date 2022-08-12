"""Sequence Processing."""
# aggregation
# find the perfect number
# perfect number: a positive integer that is qual to the sum of its divisors
def divisors(n):
    """
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [1] + [x for x in range(2,n) if n % x == 0]


def perfect_nums(max_range):
    """
    Return perfect numbers within the max_range.
    >>> perfect_nums(1000)
    [6, 28, 496]
    """
    return [n for n in range(1, 1000) if sum(divisors(n)) == n]


# compute the minimum perimeter of a rectangle, given its area
def width(area, height):
    assert area % height == 0
    return area // height


def perimeter(width, height):
    return 2 * width + 2 * height


def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area,h),h) for h in heights]
    return min(perimeters)


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
print(mul, [2,4,8],1)


# find perfect number using these higher-order functions
def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))


from operator import add
def sum_of_divisors(n):
    return reduce(add, divisors_of(n),0)


def perfect(n):
    return sum_of_divisors(n) == n
