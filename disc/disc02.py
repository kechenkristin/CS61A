def and_add(f,n):
    """Return a new function. This new function takes an argument x and returns f(x)+n"""
    def new_func(x):
        return f(x) + n
    return new_func
