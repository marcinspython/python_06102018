def drukuj_linie():
    print("-" * 40)
    # return None

drukuj_linie()
# --------------------------------------------

def zwroc_wartosc_wpisana():
    wartosc = input("Podaj wartosc")
    return wartosc

x = zwroc_wartosc_wpisana()

print(x)
# --------------------------------------------
def sumator(a,b):
    return a
# --------------------------------------------
def kalkulator(a,b, operacja="+"):
    if operacja == "+":
        return a+b

print(kalkulator(1,2))
print(kalkulator(1,2, "-"))
# --------------------------------------------
