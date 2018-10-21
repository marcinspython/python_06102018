# a = int(input("Podaj a "))
# b = int(input("Podaj b "))
# c = int(input("Podaj c "))

print("Podaj 3 wymiary [cm]: ")

a = int(input())
b = int(input())
c = int(input())


objetosc = a * b *c
dop_objetosc = 1000

if objetosc > dop_objetosc:
    print(f"Super! Jest OK bo objętość zbiornika wynosi: {objetosc}" )
elif objetosc == dop_objetosc:
    print(f"Bingo!!! wygrałeś nagrodę - masz taki sam zbiornik o pojemności {objetosc}")
else:
    print("Cieniutko :)")
