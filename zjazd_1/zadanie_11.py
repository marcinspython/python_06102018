# plansza = input("Podaj wielkość planszy [0-1000]: ")

plansza = ("100 x 100")
print(plansza)

pozycja_X = int(input("Podaj pozycję X "))
pozycja_Y = int(input("Podaj pozycję Y "))


# prawy_górny_róg = pozycja_X >= 90 and pozycja_Y >= 90
# prawy_dolny_róg = pozycja_X >= 90 and pozycja_Y >= 10
# lewy_górny_róg = pozycja_X <= 10 and pozycja_Y >= 90
# lewy_dolny_róg = pozycja_X <= 10 and pozycja_Y <= 10

if pozycja_X >= 90 and pozycja_Y >= 90:
    print("PGR")
elif pozycja_X >= 90 and pozycja_Y >= 10:
    print("PDR")
elif pozycja_X <= 10 and pozycja_Y >= 90:
    print("LGR")
elif pozycja_X <= 10 and pozycja_Y <= 10:
    print("LDR")
else:
    print("Jesteś poza planszą")




print(pozycja_X, pozycja_Y)
