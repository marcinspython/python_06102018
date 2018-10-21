a = 3
b = 9
h = 6.5


def pole_trapezu(a, b, h):
    """
    Liczy pole trapezu
    :param a: podstawa 1 - numeric
    :param b: podstawa 2 - numeric
    :param c: wysokosc - numeric
    :return:
    """
    return ((a + b) / 2) * h


def test_pole_trapezu():
    assert pole_trapezu(3, 9, 6.5) == 39.0
