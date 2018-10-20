# dodaj produkt
produkty = {"ziemniaki": 2, "bataty": 4, "pomidory": 6}
magazyn = {"ziemniaki": 10, "bataty": 10, "pomidory": 10}
do_zaplaty = 0 

while True:  # 2 dodanie while
    print("-" * 40)
    print("Nasz zielnik oferuje: ")
    for produkt in produkty.items():
        name, cena = produkt
        print(f' - {name} - {cena} PLN')
    print()

    komenda = input("Co chcesz zrobić: [d]odac, [k]upić, [koniec] by przerwać zakupy: ")  # 2
        if komenda == 'koniec':  # 2
            break
        produkt_wybrany = input("Co chcesz kupić? ")
        if produkt_wybrany not in produkty:
            print("Nie mamy takiego produktu!")
            continue

        waga = float(input(f"Ile chcesz kupić wybranego produktu {[produkt_wybrany]}: "))
        if magazyn[produkt_wybrany] < waga:
            print(f"Mamy za mało [{produkt_wybrany}], pozostało {magazyn[produkt_wybrany]} kg")
            continue
        magazyn[produkt_wybrany] = magazyn[produkt_wybrany] - waga
        cena = produkty[produkt_wybrany]
        koszt = waga * cena
        do_zaplaty += koszt
    elif komenda == 'd':
        produkt_do_dodania = input("Jaki produkt chcesz dodać?")
        if produkt_do_dodania not in magazyn:
            magazyn[produkt_do_dodania] = 0
            cana_nowego_produktu = float(input("Za ile sptrzedajemy?"))
            produkty[produkt_do_dodania] = cena_nowego_produktu
        ile_produktu_dodajemy = float(input("Ile tego dodać?"))
    else:
        print("Zła komneda")

    print(f"Wyliczony koszt to: {koszt}")
print("=" * 50)
print(f"Za zakupy zaplacisz:  {do_zaplaty} PLN")