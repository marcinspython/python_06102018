##### 01.12.2018
- C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\materialy\szablony_cwiczen.zip
numpy
pandas (data frame)
---------------------------------------------------------
pip install numpy
pip install pandas
jupyter
komenda w terminalu: `jupyter-notebook` otwiera w przegladarce 
NumPy
www.numpy.org
import numpy as np
wszystkie elementy/obiekty muszą być jednego typu

tablica array
`a = np.array([0,1], [2,3])`

zeros - tablice wypełnione zerami
`np.zeros(5)
 np.zeros((2,3))`
`np.ones(1)` -z jedynkami
`np.arange(5)`
`np.array(range(5))`
a
a.shape
a.reshape(6)

np.arange(20).reshape(4,5)

a.T -transpozycje (to co było wierszem jest kolumna)

linspace
np.linspace(0, 2, 9)

np.pi

np.linspace()

-------

ndarray

--------
shape -wymiary tablicy
a.shape
np.ones(5).shape

ndim - ilosc wymiarow 
a.ndim

size -rozmiar
a.size (pomnozenie liczb z shape)

---
dostępne typy dtypes
intp
int8
uint8
int64
float16
float

a.dtype
b.dtype

c = np.array([true, false])
c.dtype

np.array([1,2,3,]).dtype
>>> dtype(float64)

a.astype(np.float) -zmiana typu z boolean na liczby
a.astype(np.bool)

d.max() -wartosc maksymalna z tablicy

np.iinfo(np.int8)

np.finfo? -gdy nie pamietamy jakie warttosci mozemy umiescic

---
itemsize

a.dtype

printowanie
print(a)

---

Podstawowe operacjre:

odejmowanie list array
mnozenie
 
A.dot(B)
A.sum()
B.max()
B.min()


A.dot?  -dokumentacja e jupyterze

---
upcasting

---
broadcasting
[0,1,2] + 5
[0,1,2] + [5,5,5]

---
operacje wzdłuż jednej osi - sumowanie wierszy, kolumn
kolumny = 0
wiersze = 1

b.sum(axis=0)

b.sum(axis=1)

b.cumsum(axis=1)

---
universal functions
- wykresy

---
Indexing, Slicing, Iterating

a = np.array([10,11,12])
a[0]

b = np.arrange(20).reshape(4,5)
b
--pobierz 2 wiersz tabeli
b[1]
b[1][2]
b[1, 2] - tak jak wyzej
b[1:2, 0:@] - tak jak wyzej ale zakresy
















---





---------------------------------------------------------
