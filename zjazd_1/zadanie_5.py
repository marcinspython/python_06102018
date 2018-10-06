miasto_A = input("Podaj miasto A: ")
miasto_B = input("Podaj miasto B: ")
dystans = float(input(f"Podaj dystans {miasto_A}-{miasto_B} :"))
cena_paliwa = float(input("Podaj cenę paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))
koszt_przejazdu = int(((dystans * spalanie) / 100) * cena_paliwa)

print(koszt_przejazdu)

print(f"Koszt przejazdu: \n {miasto_A}, {miasto_B}, \n to {koszt_przejazdu}")

output = f"""
Miasto A: {miasto_A}
Miasto B: {miasto_B}
Dystans: {miasto_A}-{miasto_B}: {dystans}
Spalanie na 100: {spalanie}

Koszt przejazdu: {koszt_przejazdu} PLN
"""

print(output)

