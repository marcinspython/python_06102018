produkty = {"ziemniaki": 2, "bataty": 4, "pomidory": 6}
magazyn = {"ziemniaki": 10, "bataty": 10, "pomidory": 10}
do_zaplaty = 0

while True:  # 2 dodanie while
    print("-" * 40)
    print("Nasz zielnik oferuje: ")
    for produkt in produkty.items():
        name, cena = produkt
        # cena = produkty[produkt]
        # print(cena)
        # print(f' - {produkt} - {produkty[produkt]} PLN') -to samo co poniżej
        # print(f' - {produkt} - {cena} PLN')
        print(f' - {name} - {cena} PLN')


    komenda = input("Co chcesz zrobić: [k]upić, [koniec] by przerwać zakupy")  # 2
    if komenda == 'koniec':  # 2
        break
    produkt_wybrany = input("Co chcesz kupić? ")
    if produkt_wybrany not in produkty:
        print("Nie mamy takiego produktu!")
        continue

    waga = float(input(f"Ile chcesz kupić wybranego produktu {[produkt_wybrany]}: "))

    cena = produkty[produkt_wybrany]
    koszt = waga * cena
    do_zaplaty += koszt

    print(f"Wyliczony koszt to: {koszt}")
print("=" * 50)
print(f"Za zakupy zaplacisz:  {do_zaplaty} PLN")
