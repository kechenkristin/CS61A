def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    """
    >>> triple(12)
    ->  <function triple at 0x102a39848> ( 12 )
    36
    """
    return 3 * x

# equal to
def triple2(x):
    return 3 * x

triple2 = trace(triple2)
