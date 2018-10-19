# liczba
# wystąpień
# samogłoski(a, e, i, o, u, y)

napis = input(f"Podaj napis zawierający samogłoski: ")
print(napis)

sam_a = napis.count("a")
sam_e = napis.count("e")
sam_i = napis.count("i")
sam_o = napis.count("o")
sam_u = napis.count("u")
sam_y = napis.count("y")
print(
    f"W wyrazie występują: "
    f"\n {sam_a} samogłoski 'a' "
    f"\n {sam_e} samogłoski 'e' "
    f"\n {sam_i} samogłoski 'i' "
    f"\n {sam_o} samogłoski 'o' "
    f"\n {sam_u} samogłoski 'u' "
    f"\n {sam_y} samogłoski 'y'")
