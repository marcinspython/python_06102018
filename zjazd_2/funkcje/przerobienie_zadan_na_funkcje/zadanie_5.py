# pobieranie danych
def pobieranie_danych():
    miasto_A = input("Podaj miasto A: ")
    miasto_B = input("Podaj miasto B: ")
    dystans = float(input(f"Podaj dystans {miasto_A}-{miasto_B} :"))
    cena_paliwa = float(input("Podaj cenę paliwa: "))
    spalanie = float(input("Spalanie na 100 km: "))
    return miasto_A, miasto_B, dystans, cena_paliwa, spalanie


def obliczenie_kosztu(miasto_A, miasto_B, dystans, cena_paliwa, spalanie):
    koszt_przejazdu = int(((dystans * spalanie) / 100) * cena_paliwa)
    return koszt_przejazdu


def drukuj_wynik(miasto_A, miasto_B, dystans, cena_paliwa, spalanie):
    output = f"""
Miasto A: {miasto_A}
Miasto B: {miasto_B}
Dystans: {miasto_A}-{miasto_B}: {dystans}
Spalanie na 100: {spalanie}

Koszt przejazdu: {koszt_przejazdu} PLN
"""
    return output


