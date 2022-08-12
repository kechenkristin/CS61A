"""self reference"""

def print_all(x):
    print(x)
    return print_all

print("print all")
print_all(1)(3)(5)


def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum

print("print sum")
print_sums(1)(3)(5)
