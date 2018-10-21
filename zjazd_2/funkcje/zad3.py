def policz_znaki(napis, start="<", stop=">"):
    wynik = 0
    poziom_zaglebienia = 0
    for znak in napis:
        if znak == start:
            poziom_zaglebienia += 1
        elif znak == stop:
            poziom_zaglebienia -= 1
        else:
            wynik += poziom_zaglebienia
    return wynik


# testy pomocnicze

def test_0_poziom_zaglebienia():
    assert poziom_zaglebienia("aaaa bbbbb cccc") == 0


def test_1_poziom_zaglebienia():
    assert poziom_zaglebienia("aaaa < bbbbb cccc") == 1


def test_policz_znaki_pusty_napis():
    assert policz_znaki('') == 0


def test_policz_napis_bez_znacznikow():
    assert policz_znaki('to jest napis') == 0


def test_policz_znaki_w_nawiasach_domyslnych_jeden_lewel():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4


def test_policz_znaki_w_dwa_levele():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18


def test_policz_znaki_w_trzy_levele():
    assert policz_znaki('a<a<a<a>>>') == 6
