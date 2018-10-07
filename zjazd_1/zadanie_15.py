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



# while True:
# #     ruch = input("Popdaj liczbę lub wpisz KONIEC by zakonczyc")
# #     if ruch.lower() == "koniec":
# #         break
# #
# # # poruszanie gracza po planszy
# # while True:
# #
# #     ruch = input()
# #
# # # w a s d
# # if ruch == 'w':
# #     pass
# # if ruch == 'a':
# #     pass
# # if ruch == 's':
# #     pass
# # if ruch == 'd':
# #     pass

# oblicz minimalną liczbę kroków po ruchu


print(f"Położenie skarbu: x={s_x}, y={s_y}")
print(f"Położenie gracza: x={g_x}, y={g_y}")
print(minimalna_liczba_krokow_po_wylosowaniu)