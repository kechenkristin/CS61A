"""Implementing the tree abstraction.
A tree has a root label and a list of branches.
Each branch is a tree."""

def tree(label, branches = []):
    # Verifies the tree definition
    for branch in branches:
        assert is_tree(branch)
    # Create a list from a sequence of branches
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    # base case
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


""" Processing a leaf is often the base case of a tree processing function.
The recursive case typically makes a recursive call on each branch, then aggregates."""
def count_leaves(tree):
    # base case
    if is_leaf(tree):
        return 1
    else:
        brach_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum[[leaves(b) for b in branches(tree)], []]


def print_tree(tree, indent = 0):
    print(' ' * indent + str(label(t)))
    for b in branches(tree):
        print_tree(b, indent + 1)


def fact(n):
    """ taking the return valuse of recursive call and manipulating it."""
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def fact_times(n, k):
    """ Build result by passing infomation into the recursive call as argument.
        Return k * n * (n-1) * ... * 1
    """
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)


numbers = tree(3, [tree(4), tree(5, [tree(6)])])

haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])


def print_sums(t, so_far):
    """ print_sums(numbers, 0)
        >>> 7
        >>> 14
    """
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


def height(t):
    """ Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)], tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])


def square_tree(t):
    """Return a tree with the square of every element in t."""
    sq_branches = [square_tree(branch) for branch in branches(t)]
    return tree(label(t)**2, sq_branches)


def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path
