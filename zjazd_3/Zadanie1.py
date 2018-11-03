"""
Zaimplementuj klase Product przechowujaca informacje o cenie,
nazwie oraz ID produktu. Zaimplementuj metode wypisujaca
informacje o produkcie na konsole.
Przykład uzycia:
>>> product = Product(1, 'Woda', 10.99)
>>> product.print_info()
Produkt "Woda", id: 1, cena: 10.99 PLN
"""


class Product(object, ID, cena):
    pass


def test_product():
    product = Product(1, 'Woda', 10.99)
    assert product.ID == 1
    assert product.nazwa == 'Woda'
    assert product.cena == 10.99

def test_product_print():
    product = Product(1, 'Woda', 10.99)
    assert product.print_info() == 'Produkt "Woda", id: 1, cena: 10.99 PLN'