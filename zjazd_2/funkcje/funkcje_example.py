
def przywitaj_sie():
    return 1

przywitaj_sie()
print(przywitaj_sie)
print(type(przywitaj_sie))
print(type(przywitaj_sie()))

print(przywitaj_sie())
# ...imiona....

# -----------------------------
def czy_wieksza_niz_3(liczba):
    if liczba>3:
        return True
    return False


# -------- testy ---------------------
def czy_wieksza_niz_3(liczba):
    if liczba > 3:
        return True
    return False

def test_wieksza_niz_3_dla_wiekszej_niz_3():
    assert czy_wieksza_niz_3(4)

def test_wieksza_niz_3_dla_mniejszej_niz_3():
    assert czy_wieksza_niz_3(4)

