def memo(f):
    """ Idea: Remember the results that have been computed before."""
    # Keys are arguments that map to return values
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    # Same behavior as f, if f is a pure function
    return memoized
