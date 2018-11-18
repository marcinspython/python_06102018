# policzyć % przeżywalność wsrod ogółu, kobiet, mężczyzn
# policzyć średnią wieku kobiet i

# TODO rkorzen....

import csv

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    dlugosci = {}
    for row in data:
        # print(row)
        dlugosci[row['Survived']] = dlugosci.get(row['Survived'], 0) + 1
    print(dlugosci)  # liczy ile kolumn ma każdy wiersz
    # ogolem przezywalnosc:
    przezylo = dlugosci['1']
    zginelo = dlugosci['0']

    print(f"Przezylo z ogółu {round(100*przezylo/(przezylo+zginelo), 2)}")
    print(f"Zginęlo z ogółu {round(100*zginelo/(przezylo+zginelo), 2)}")
