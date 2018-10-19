# liczba
# wystąpień
# samogłoski(a, e, i, o, u, y)

napis = input(f"Podaj napis zawierający samogłoski: ")
print(napis)

for i in napis:
    if i == "a":
        print("To jest 'a'")
        print(len(napis))
        continue
    elif i == "e":
        print("To jest 'e'")
        continue
else:
    print("W wyrazie nie ma samogłosek")
