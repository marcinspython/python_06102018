class Animal:
    gatunek = "Canis Lupus"

    def __init__(self, gatunek):
        self.gatunek = gatunek



azor = Animal("Canis Familianis")
rudolf = Animal("Ragnifer Tarandus")

print(azor)
# print(type(azor))
# print(dir(azor))
print(azor.gatunek)
print(rudolf.gatunek)