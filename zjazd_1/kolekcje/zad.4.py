# wypisuje liczby od 0 do 100
# for i in range(101):
#     print(i)

podzielna = 0
# wypisuje liczby od 0 do 100 podzielne przez 3 lub podzielne przez 5
for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        # print(i)
        podzielna += 1

# napisz ile liczb wystąpiło w tym przedziale

print(podzielna)

print(f"W przedziale 0-100 liczb jest {podzielna} liczb podzielnych przez 3 i 5")




# sposób rkorzen
# wypisać
lista = list(range(101))
wynik = []
for el in lista:
    for el%3 == 0 or el%5 == 0:
        wynik.append(el)

print(len(wynik))
