"""curring, function takes  mutiple arguments into a chain of functions that each take a single argument."""

def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h

curried_pow(2)(3)

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1

map_to_range(0, 10,curried_pow(2))
