""" Functions as returned values."""

def square(x):
    return x * x

def successor(x):
    return x + 1

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

square_successor = compose1(square, successor)
result = square_successor(12)
print("square of (12 + 1)",result)

