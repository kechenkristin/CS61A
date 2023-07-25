Class Radio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Radio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        # Type Dispatching: Inspect the type of an argument in order to
        # select behavior
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom

        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom

        # Type Coercion: Convert one value to match the type another
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Radio(n//g, d//g)


    __radd__ = __add__


def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n - d)
    return n
