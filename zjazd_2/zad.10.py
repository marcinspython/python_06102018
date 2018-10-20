napis = input("Podaj napis: ")
liczniki_liter = {}
# w podanym napisie zliczyć wystapienia poszczegolnych liter

# zliczyć
for litera in napis:
    if litera in liczniki_liter:
        liczniki_liter[litera] = liczniki_liter[litera] + 1
    else:
        liczniki_liter[litera] = 1

# zliczyć 2 razy
for litera in napis:
    liczniki_liter[litera] = liczniki_liter.get(litera, 0) + 1

#wynik
for litera in liczniki_liter:
    print(f"litera: {litera} wystąpiła {liczniki_liter[litera]} razy")