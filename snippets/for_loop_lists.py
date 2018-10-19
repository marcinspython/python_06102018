lista = ["a", "b", "z", "d", "e"]

for litera in lista:
    print(litera)
# -------------------------------
print("Second example")

for litera in lista:
    if litera == "c":
        print(f"To jest litera 'c': = {litera}")
        break
else:
    print("nie znaleziono litery 'C' ")
# -------------------------------
