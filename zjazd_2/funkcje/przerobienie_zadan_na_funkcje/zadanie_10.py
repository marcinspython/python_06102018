# print("Podaj dwie liczby:  ")
# a = int(input())
# b = int(input())
# print("Rodzaj operacji:  ")
# c = str(input())
#
# dod = a + b
# odj = a - b
# mnz = a * b
# dziel = a / b
#
# if c == "+":
#     print(dod)
# else:
#
# print(a, b, c)

liczba_1 = int(input("Podaj liczbę pierwszą"))
liczba_2 = int(input("Podaj liczbę druga"))
operacja = input("Rodzaj operacji: ")

if operacja == "+":
    # pass
    wynik = liczba_1 + liczba_2
elif operacja == "-":
    # pass
    wynik = liczba_1 - liczba_2
elif operacja == "/":
    if liczba_2 == 0:
        raise ValueError("Nie dziel przez zero!!!")
    wynik = liczba_1 / liczba_2
elif operacja == "*":
    wynik = liczba_2 * liczba_1
else:
    # print(("wybrałeś niezrozumiała operację"))
    raise ValueError("Nieprawidłowa wartość dla parametru operacji")

print("Wynik operacji iiiii: ", wynik)
