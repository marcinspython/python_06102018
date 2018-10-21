# ----------------------------------------------------------------------------


def formatuj(cena, *args):
    out = []
    for text in args:
        text = text.replace('$cena', str(cena))
        out.append(text)
    return "\n".join(out)


def test_formatuj():
    assert formatuj(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10,
    ) == "koszt 10 PLN\nkwota 10 brutto"

    assert formatuj(
        10,
        'koszt $cena PLN',
        'kwota $cena brutto',
        'sumarycznie $cena',
        cena=10,
    ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10"
