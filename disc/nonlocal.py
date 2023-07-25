def memory(n):
    def help(f):
        nonlocal n
        n = f(n)
        return n
    return help
