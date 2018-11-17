#### 17.11.2018
###Pakiety i moduły
`from sys`
from zjazd_3.Zadanie6 import Vector

from zjazd_4.mathematica.mathematica.geometry.figures import square_area
from zjazd_4.mathematica.mathematica.geometry.figures import triangle_area


def test_square_area():
    assert square_area(5) == 25


def test_triangle_area():
    assert triangle_area(4, 5) == 10

def square_area(n):
    return n ** 2


def triangle_area(base, height):
    return (base * height) / 2

