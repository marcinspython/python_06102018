moja_tupla = (2, 3, 4, 5, 6, 8, 2, 3, 1, 9)
print(moja_tupla)
print(len(moja_tupla))

print(moja_tupla[1]) #drugi element
assert 3 == moja_tupla[1]

print(moja_tupla[-2])
print(moja_tupla[2:7])
# assert (3, 4, 5, 6, 8, ) == moja_tupla[2:7]
print(moja_tupla[::3])
print(moja_tupla[::-2])

#pusta tupla
x = tuple()
