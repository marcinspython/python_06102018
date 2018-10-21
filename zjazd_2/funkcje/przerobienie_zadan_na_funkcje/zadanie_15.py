from random import randint

# wylosuj położenie skarbu
s_x = randint(1, 10)
s_y = randint(1, 10)
print(f"Skarb: {s_x}, {s_y}")

# wylosuj początkowe położenie gracza
g_x = randint(1, 10)
g_y = randint(1, 10)
print(f"Gracz: {g_x}, {g_y}")
# oblicz minimalną liczbę kroków pomiędzy graczem a skarbem
minimalna_liczba_krokow_po_wylosowaniu = abs(s_x - g_x) + abs(s_y - g_y)

# zapisz w zmiennej

# ustaw poczatkowa liczbe ruchów na 0
liczba_ruchów = 0

# mechanika
while True:
    min_1_ruch_przed = abs(s_x - g_x) + abs(s_y - g_y)

# poruszanie gracza po planszy
while True:
    min_1_ruch_przed = abs(s_x - g_x) + abs(s_y - g_y)
    ruch = input("Wykonaj ruch [wasd]")
    ruch = ruch.upper()

# w a s d
if ruch == 'w':
    g_y += 1
if ruch == 'a':
    g_x -= 1
if ruch == 's':
    g_y -= 1
if ruch == 'd':
    g_x += 1
# wyjście poza planszę
if g_x > 10 or g_y > 10 or g_x < 1 or g_y < 1:
    print("Wyszedłeś poza planszę")

# oblicz minimalną liczbę kroków po ruchu
min_1_ruch_po = abs(s_x - g_x) + abs(s_y - g_y)

# sparawdz czy znalazł skarb
    if min_1_ruch_po == 0:
        print("Wygrałeś")
        break

# określ czy się przybliża czy oddala
if min_1_ruch_po > min_1_ruch_przed:
    print("Zimno")
if min_1_ruch_po < min_1_ruch_przed:
    print("Ciepło")

print(f"Położenie skarbu: x={s_x}, y={s_y}")
print(f"Położenie gracza: x={g_x}, y={g_y}")
print(minimalna_liczba_krokow_po_wylosowaniu)
