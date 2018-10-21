print(locals())
print(globals())
# ---------------------------------------------------------------------------------
return - kończy funkcje
www.packtpub.com / zcientific computing with python3
przeróbki zadna na funkcyjne - zp oprzeniego zjazdu;
print i return z funkcji by zrobić assertion - czuy wydrukowało sie to co trzeba

zad.5
dane = pobieranie_danych()
*dane (rozpakowanie tupli)
koszt = obliuczenie_kosztu(*dane)

zad.10 przeróbka
dane = podaj_liczby_i_operacje()
kalkulator(*dane)

# obsługa błędu
def prezentuj_wynik():
    danie = podaj_liczby_i_operacje()
    try:
        wynik = kalkulator(*dane)
    except ValueError:
        wynik = "Operacja niedozwolona"
    print(wynik)

zad.13 przeróbka
dir([]) -linia komend
# -----------------
dir([])
Out[3]:
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']

# -----------------















