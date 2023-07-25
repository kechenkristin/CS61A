def rec(x,y):
    if y <= 0:
        return 1
    else:
        return x * rec(x, y - 1)
