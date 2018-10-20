my_dict = {
    "pierwsza": "a",
    "druga": "b"
}

# dodawanie
my_dict['trzecia'] = 'c'

# ----------------------
d2 = dict()
d2 = dict([('a', 1), ('b', 2)])
print('d2', d2)
# ----------------------

print((my_dict['pierwsza']))
print((my_dict['druga']))

print(type(my_dict))
print((my_dict.items()))
print((my_dict.keys()))
print((my_dict.values()))

# ----------------------
produkt1 = {'nazwa': "Koper", 'cena': 3}
produkt2 = {'nazwa': "Koper2", 'cena': 2}

produkty = [produkt1, produkt2]

