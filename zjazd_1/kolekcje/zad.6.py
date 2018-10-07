# ymieniajcz miejscami w yadanej liscie licyb

liczby = [5, 2, 1, 4, 3]

min_i = None
max_i = None

print(liczby)
# print(list(range(len(liczby))))
indeksy = (list(range(len(liczby))))

for i in indeksy:
    if min_i == None or liczby[i] < liczby[min_i]: # porównuje liczbe z listy z wartosciua indeksu!!!
        min_i = i         # debugger - uruchomi test przy min_i = i
    if max_i == None or liczby[i] > liczby[max_i]:
        max_i = i
        print(f"i= {i}")
        print(f"max_i = {max_i}")
# zamień miejscami

if min_i is not None and max_i is not None:
    tmp = liczby[min_i]
    liczby[min_i] = liczby[max_i]
    liczby[max_i] = tmp

# 2 sposób  w jednej linii - zamiana miejscami
liczby[min_i], liczby[max_i] = liczby[max_i], liczby[min_i]



# assert liczby2 == [1,2,5,4,3]