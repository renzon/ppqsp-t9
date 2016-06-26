from numbers import Real


class Vetor:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __repr__(self):
        return 'Vetor(%r,%r)' % (self.x, self.y)

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, n):
        if isinstance(n, Real):
            return Vetor(self.x * n, self.y * n)
        return NotImplemented

    def __rmul__(self, n):
        return self * n


v = Vetor(1, 2)
v2 = Vetor(2, 2)

print(v + v2)
print(v)
print(v2)
print(v * 3)
print(4 * v)
print(id(v))
v += v2
print(id(v))
print(v)
