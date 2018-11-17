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

print(__name__)
if __name__ = "main__"

http://api.nbp.pl/api/exchangerates/tables/A/?format=json
-----
import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A/?format=json") as f:
    print(f)
    kursy = json.loads(f.read())

rates = kursy[0]['rates']
for r in rates:
    print(f"{r['code']} - {r['mid']}")
-----------
import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A/?format=json") as f:
    print(f)
    kursy = json.loads(f.read())

rates = kursy[0]['rates']
for r in rates:
    print(f"{r['code']} - {r['mid']}")

######

waluta = input("Jaka waluta z powyższej listy")
ile = float(input(f"Ile hcesz kupic {waluta}?"))

for r in rates:
    if r['code'] == waluta:
        result = ile *r['mid']

print("płacisz", result)
---------------------------
www.metaweather.com/api/
---------------------------
