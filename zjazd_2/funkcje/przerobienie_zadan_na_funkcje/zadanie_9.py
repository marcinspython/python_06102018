import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)

rok_urodzenia = int(input("Podaj rok: "))
wiek = now.year - rok_urodzenia

if wiek >= 18:
    print("TAK Jesteś pełnoletni")
else:
    print("Jesteś NIE_pełnoletni!!!")
