(1, 2, 3)
('abc', 1, 99.99)

# ##### pusta tupla jedynie przez konstruktor #####
tuple()

# ##### operator dostępu // nawiasy kkwadratowe z indeksem w środku [] #####
uczestnicy = ('Jan', 'Piotr', 'Ola', 'Tomasz', 'Sylwia')
# uczestnicy[0]
print(f'operator dostępu: {uczestnicy[0]}')
print(f'operator dostępu: {uczestnicy[2]}')
print(f'operator dostępu: {uczestnicy[4]}')
# print(uczestnicy[11]) # IndexError:

# ##### indeksowanie od tyłu kolekcji // ze znakiem "-" #####
uczestnicy = ('Jan', 'Piotr', 'Ola', 'Tomasz', 'Sylwia')
print(f'tupla uczestnicy = {uczestnicy}')
uczestnicy[-1]
print(f'indeksowanie od tyłu kolekcji dla -1: {uczestnicy[-1]}')
print(f'indeksowanie od tyłu kolekcji dla -2: {uczestnicy[-2]}')
print(f'indeksowanie od tyłu kolekcji dla -5: {uczestnicy[-5]}')
