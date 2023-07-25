class Tree:
    """ A Tree has a label and a list of branches; each branch is a Tree.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)


    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)


    def __str__(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append(' ' + line)
        return [str(self.label)] + lines


    def is_leaf(self):
        return not self.branches
        

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b: 
                return True
        return False


    def map(self, fn):
        """ Apply a function fn to each node on the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


def count_leaves(t):
    """
    >>> count_leaves(Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])]))
    3
    """
    if t.is_leaf():
        return 1
    else:
        branch_counts = [count_leaves(b) for b in t.branches]
        return sum(branch_counts)


def leaves(t):
    """ Return a list of leaf labels in Tree T."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves


def height(t):
    """ Return the number of transitions in the longest path in T.

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    """
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])


def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corrsponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    if t.is_leaf():
        return
    else:
        for b in t.branches:
            cumulative_mul(b)
            t.label *= b.label
        return 


def square_tree(t):
    """Return a tree with the square of every element in t.

    >>> numbers = Tree(1, [Tree(3, [Tree(5)]), Tree(2)])
    >>> square_tree(numbers)
    Tree(1, [Tree(9, [Tree(25)]), Tree(4)])
    """
    sq_branches = [square_tree(b) for b in t.branches]
    return Tree(t.label ** 2, sq_branches)


def find_path(t, x):
    """
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    """
    if t.label == x:
        return [t.label]
    else:
        for b in t.branches:
            path = find_path(b, x)
            if path:
                return [t.label] + path
