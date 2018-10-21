liczba = int(input("Podaj liczbę: "))

# print(liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10 or liczba == 7)

liczba_podzielna_2 = liczba % 2 == 0
liczba_podzielna_3 = liczba % 2 == 0
wieksza_niz_10 = liczba > 10
rowna_7 = liczba == 7

print(liczba_podzielna_2, liczba_podzielna_3, wieksza_niz_10, rowna_7)

wynik = (liczba_podzielna_3 and
         liczba_podzielna_2 and
         wieksza_niz_10) or rowna_7


# wynik = liczba_podzielna_3 and \
#          liczba_podzielna_2 and \
#          wieksza_niz_10 or rowna_7

print(wynik)
