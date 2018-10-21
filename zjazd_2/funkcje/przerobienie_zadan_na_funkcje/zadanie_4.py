# a = 10.0
# b = 2.5
#
# c = a * b
#
# print(f"Należność: {c}")
#
# output = f"Cena: {a} \nWaga: {b} \nNależność: {c}"
# print(output)

def naleznosc(a, b):
    """
    Wylicza należność:
    :param a: cena - numeric
    :param b: waga - numeric
    :return:
    """
    return a * b


def drukuj(a, b):
    output = f"Cena: {a} \nWaga: {b} \nNależność: {naleznosc(a, b)}"
    print(output)
    return output

drukuj(2.5, 10)


def test_naleznosc():
    assert naleznosc(10, 2.5) == 25
#
# def test_drukuj():
#     assert drukuj()......