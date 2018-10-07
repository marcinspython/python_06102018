liczby = []

# zebranie liczb
while len(liczby) < 10:
    nowa_liczba = int(input("Podaj: "))
    liczby.append(nowa_liczba)



# obliczenie sredniej
srednia = sum(liczby)/len(liczby)




# wypisanie wyniku
print(srednia)
