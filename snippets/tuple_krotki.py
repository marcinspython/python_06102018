print('//--- tuple ------------------------------------------------------------')
(1, 2, 3)
('abc', 1, 99.99)

# ##### pusta tupla jedynie przez konstruktor #####
tuple()
print(
    '//--- pusta tupla tuple() -----------------------------------------------')

# ##### operator dostępu // nawiasy kkwadratowe z indeksem w środku [] #####
uczestnicy = ('Jan', 'Piotr', 'Ola', 'Tomasz', 'Sylwia')
print(f'tupla uczestnicy = {uczestnicy}')
# uczestnicy[0]
print(f'operator dostępu: {uczestnicy[0]}')
print(f'operator dostępu: {uczestnicy[2]}')
print(f'operator dostępu: {uczestnicy[4]}')
# print(uczestnicy[11]) # IndexError:
print('//----------------------------------------------------------------------')

# ##### indeksowanie od tyłu kolekcji // ze znakiem "-" #####
uczestnicy = ('Jan', 'Piotr', 'Ola', 'Tomasz', 'Sylwia')
print(f'tupla uczestnicy = {uczestnicy}')
uczestnicy[-1]
print(f'indeksowanie od tyłu kolekcji dla -1: {uczestnicy[-1]}')
print(f'indeksowanie od tyłu kolekcji dla -2: {uczestnicy[-2]}')
print(f'indeksowanie od tyłu kolekcji dla -5: {uczestnicy[-5]}')
# print(f'indeksowanie od tyłu kolekcji dla -5: {uczestnicy[-6]}') # IndexError: tuple index out of range
print('------------------------------------------------------------------------')
# ##### wycinanie #####
print('//--- wycinanie --------------------------------------------------------')
uczestnicy = ('Jan<0/-4>', 'Piotr<1/-4>', 'Ola<2/-3>', 'Tomasz<3/-2>', 'Sylwia<4/-1>')
print(f'tupla uczestnicy = {uczestnicy}')
print(f'tupla uczestnicy [1:3] = {uczestnicy[1:3]}')
print(f'tupla uczestnicy [2:4] = {uczestnicy[2:4]}')
print(f'tupla uczestnicy [:3] = {uczestnicy[:3]}')
print(f'tupla uczestnicy [2:] = {uczestnicy[2:]}')
print(f'tupla uczestnicy [:-1] = {uczestnicy[:-1]}')
print(f'tupla uczestnicy [-2:] = {uczestnicy[-2:]}')

print('//--- wycinanie z podanym krokiem (trzeci argument) --------------------')
uczestnicy = ('Jan<0/-4>', 'Piotr<1/-4>', 'Ola<2/-3>', 'Tomasz<3/-2>', 'Sylwia<4/-1>')
print(f'tupla uczestnicy = {uczestnicy}')
print(f'tupla uczestnicy [0:4:2] = {uczestnicy[0:4:3]}')

print("c.d.n")



print('//--- funkcja len() -----------------------------------------------------')

