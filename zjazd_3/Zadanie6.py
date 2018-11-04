# dodawanie +
# odejmowanie -
# równość ==
# mniejsze niż < (po długości)
# mnożenie (przez skalar) *
    # vector_1 = Vector(x=1, y=2)
    # vector_2 = Vector(x=1, y=2)
    # vector_3 = vector_1 + vector_2


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def test_vector_add():
    v1 = Vector(1,3)
    v2 = Vector(4,7)
    result = v1 + v2
    assert result.x == 5
    assert result.y == 10

def test_vector_sub():
    v1 = Vector(1,3)
    v2 = Vector(4,7)
    result = v1 - v2
    assert result.x == -3
    assert result.y == -4

def test_vector_equal():
    v1 = Vector(1,3)
    v2 = Vector(1,3)
    v3 = Vector(4,7)
    assert v1 == v2
    assert not (v1 == v2)

