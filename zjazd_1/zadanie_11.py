# plansza = input("Podaj wielkość planszy [0-1000]: ")

plansza = ("100 x 100")
print(plansza)

X = int(input("Podaj pozycję X "))
Y = int(input("Podaj pozycję Y "))

centrum = X > 10 and Y < 90 and X < 90 and Y < 90
# prawy_górny_róg = pozycja_X >= 90 and pozycja_Y >= 90
# prawy_dolny_róg = pozycja_X >= 90 and pozycja_Y >= 10
# lewy_górny_róg = pozycja_X <= 10 and pozycja_Y >= 90
# lewy_dolny_róg = pozycja_X <= 10 and pozycja_Y <= 10

if X >= 90 and Y >= 90:
    print("PGR")
elif X >= 90 and Y >= 10:
    print("PDR")
elif X <= 10 and Y >= 90:
    print("LGR")
elif X <= 10 and Y <= 10:
    print("LDR")
else:
    print("Jesteś poza planszą")

print(X, Y)


