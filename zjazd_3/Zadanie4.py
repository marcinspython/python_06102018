"""
basket = Basket()
product = Product(1, 'Woda', 10.00)
basket.add_product(product, 5)
basket.count_total_price()
50.0
basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00'
"""

print("*" *100)

class Basket(object):

    def __init__(self):
        self.produkty = []

    def __str__(self):
        return "Basket"
    pass

def test_create_basket():
    basket = Basket()
    assert str(basket) == "Basket"
    assert basket.produkty == []

def test_add_product_to_basket():
    basket = Basket()

