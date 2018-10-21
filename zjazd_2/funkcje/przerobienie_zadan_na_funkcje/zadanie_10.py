def podaj_liczby_i_operacje():
    liczba_1 = int(input("Podaj liczbę pierwszą"))
    liczba_2 = int(input("Podaj liczbę druga"))
    operacja = input("Rodzaj operacji: ")
    return liczba_1, liczba_2, operacja


def kalkulator(liczba_1, liczba_2, operacja):
    wynik = "nieustalony wynik"

    if operacja == "+":
        # pass
        wynik = liczba_1 + liczba_2
    elif operacja == "-":
        # pass
        wynik = liczba_1 - liczba_2
    elif operacja == "/":
        if liczba_2 == 0:
            raise ValueError("Nie dziel przez zero!!!")
        wynik = liczba_1 / liczba_2
    elif operacja == "*":
        wynik = liczba_2 * liczba_1
    else:
        # print(("wybrałeś niezrozumiała operację"))
        raise ValueError("Nieprawidłowa wartość dla parametru operacji")

    print("Wynik operacji iiiii: ", wynik)

def prezentuj_wynik():
    danie = podaj_liczby_i_operacje()
    try:
        wynik = kalkulator(*dane)
    except ValueError:
        wynik = "Operacja niedozwolona"
    print(wynik)

dane = podaj_liczby_i_operacje()
kalkulator(*dane)