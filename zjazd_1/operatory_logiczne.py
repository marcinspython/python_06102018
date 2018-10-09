# a = 9
# b = 3
#
# print("Wynik1 ", a > b and a % b == 0)
#
# print("Wynik2 ", a > b or a > 7)
#
# print("Wynik3 ",not a < 10)



# petle if else

a = int(input("Podaj a"))
b = int(input("Podaj b"))

if a > b and a % b == 0:
    print(f"liczba {a} jest wieksza od {b} i jest przez {b} podzielna")
elif a == b:
    print(f"liczba a jest równa liczbie b i wynosi: {a}")
else:
    print("haha")