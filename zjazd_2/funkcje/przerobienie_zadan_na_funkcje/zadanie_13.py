# 1 pobrać dane

# 3 ustalić min i max
numer_dnia = 1

suma_temperatur = 0
min_ = None
max_ = None

def pobieranie_danych(ile_razy=7):
    temperatury = []
    for i in range(ile_razy):
        temp = int(input(f"Podaj tempoerature z dnia {i+1}: "))
        temperatury.append(temp)
    return temperatury


# 2 policzyć srednia
def srednia_temp(tempertaury):
    srednia_temperatura = sum(tempertaury) / len(tempertaury)
    return srednia_temperatura

def znajdz_ekstrema(temperatury):
    min_ = min(temperatury)
    max_ = max(temperatury)
    return min_, max_

# 4 zaprezentować
def prezentuj_dane(srednia):
    print(f'Srednia temperatura w tygodniu to {srednia_temperatura}')
    print(f'Temp minimalna to było: {min_}')
    print(f'Temp maxymalna to było: {max_}')

dane = pobieranie_danych()
sr_temp = srednia_temp(dane)
min_, max_ = znajdz_ekstrema(dane)
prezentuj_dane(sr_temp, min_, max_)

