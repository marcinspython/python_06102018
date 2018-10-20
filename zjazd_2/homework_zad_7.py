napis = input("Podaj napis: ")
SAMOGLOSKI = 'aeiou'
ile_samogłosek = 0

for znak in napis:
    # jesli samogloska to  powieksz licznik
    if znak in SAMOGLOSKI:
        ile_samogłosek += 1

print(f"W tekście : {napis} znajduje się {ile_samogłosek} samogłosek")