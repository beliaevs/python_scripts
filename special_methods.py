import collections
import math

class Indexer(object):
    def __init__(self):
        self._indices = [k for k in range(10)]

    def __getitem__(self, idx):
        return 2 * self._indices[idx]

    def __len__(self):
        return len(self._indices)


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, a):
        x = self.x + a.x
        y = self.y + a.y
        return Vector(x, y)

    def __mul__(self, a):
        return Vector(self.x * a, self.y * a)

    def __rmul__(self, a):
        return Vector(self.x * a, self.y * a)

    def __repr__(self):
        return f'Vector({self.x!r},{self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

def main():
    a = Indexer()
    print(a[0], a[1], a[2])
    print(f'len = {len(a)}')

    for i in a:
        print(i)

    Card = collections.namedtuple('Card', ['Rank', 'Suit'])
    c = Card(10, 'Daggers')
    print(c)

    v = Vector(1,2)
    w = Vector(3,4)
    u = 3 * v + w * 2
    print(v, w, u)
    print(abs(Vector(3, 4)))

if __name__=='__main__':
    main()