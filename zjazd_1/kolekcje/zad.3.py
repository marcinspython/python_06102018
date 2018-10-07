lista = [-1, 100, 20, 30, 15, -14, -5]

# liczniki

licznik_ujemnych = 0
licznik_dodatn = 0

for el in lista:
    if el <0:
        licznik_ujemnych+=1
    elif el>0:
        licznik_dodatn+=1



# na listach

dodatnie = []
ujemne = []

for el in lista:
    if el <0:
        dodatnie.append(el)
    elif el>0:
        ujemne.append(el)

# wydruk wyników

print("dodatnich:", licznik_dodatn)
print("ujemne:", licznik_ujemnych)

print("dodatnich:", len(dodatnie))
print("ujemne:", len(ujemne))

