my_text = input("Podaj tekst ")
# 1 sposób
nawias1 = 0
nawias2 = 0

    if i == "<":
        nawias1 = index
    if i == ">":
        nawias2 = index
print(nawias2 - nawias1 - 1)

# 2 sposób

czy_miedzy_nawiasami = False
licznik = 0

for znak in my_text:
    if znak == "<":
        czy_miedzy_nawiasami = True
    elif znak == ">":
        czy_miedzy_nawiasami = False
    elif czy_miedzy_nawiasami:
        licznik += 1
print(licznik)
