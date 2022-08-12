"""Generalization"""

def make_adder(n):
    def adder(k):
        return k + n
    return adder

add1 = make_adder(1)
print(add1(2))

print(make_adder(1)(2))
