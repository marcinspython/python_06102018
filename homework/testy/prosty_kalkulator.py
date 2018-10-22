def dodawanie_calc(a, b):
    return a+b


def odejmowanie_calc(a, b):
    return a-b


def mnozenie_calc(a, b):
    return a * b


def dzielenie_calc(a, b):
    return a / b


def test_dodawanie():
    assert dodawanie_calc(2, 2) == 4


def test_odejmowanie():
    assert odejmowanie_calc(2, 2) == 0


def test_mnozenie():
    assert mnozenie_calc(3, 3) == 9


def test_dzielenie():
    assert dzielenie_calc(10, 2) == 5
