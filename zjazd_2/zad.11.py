liczby = set()

while True:
    komenda = input("Wprowadz liczbe lub [k] by zakonczyc ")
    if komenda == 'k':
        break
    liczba = int(komenda)
    liczby.add(liczba)

print(len(liczby & set(range(2, 101, 2))))
