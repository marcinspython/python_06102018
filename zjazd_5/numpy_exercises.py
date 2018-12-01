import numpy as np

# zadania z pliku numpy.ipynb

# Indeksowanie, wycinanie, iterowanie - Indexing, Slicing and Iterating

# Stwórz liste sześcianów liczb od 0 do 9
a = np.arange(10) ** 3

# wybierz z listy zaznaczone elementy
a[2:5]

a[:5:2]

# przekształć by otrzymać wynik
a[:5:2] = -1000

# Odwróć listę
a[::-1]

# Sprawdź typ
a.dtype

# W pętli for wyprintuj dla każdego elementu pierwiastek sześcienny z elementy
# for i in a:
#     print(i ** (1/3))

# Stwórz macierz 10x10 z kwadratami liczb od 1 do 100

m = np.arange(1, 101).reshape(10,10)
print(m)

# Stwórz macierz 5x5 gdzie na krawędziach będą 0 a w środku 1
### pierwszy sposób
n = np.ones([5,5])
n[0] = 0
n[-1] = 0
n[1][0] = 0
# for row in n:
#     row[0] = 0
#     row[-1] = 0
print(n)
### drugi sposób
o = np.zeros([5,5])
o[1:-1, 1:-1] = 1
print(o)

# Stwórz tabliczkę mnożenia liczb od 0 do 9 w postaci dwuwymiarowej macierzy
x = np.arange(4)
y = x.reshape(4,1)
print(x*y)

x = np.arange(10)
y = np.arange(10,1)
print(x*y)