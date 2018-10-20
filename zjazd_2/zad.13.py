# -------kwadraty - 1 sposób --------------------------------
kwadraty = [x ** 2 for x in range(1, 101)]
print(kwadraty)
# --------kwadraty 2 sposób --------------------------------
kwadraty = []
for x in range(1, 101):
    kwadraty.append(x ** 2)
print(kwadraty)
# --------------------------------------------------------------
print([i / 10 for i in range(11)])

# ----- zbior tupli---------------------------------------------------------
zbiór_tupli = {(x, x ** 2, x ** 3) for x in range(1, 101)}
print(zbiór_tupli)

# --- słownik mapujacy napisy ------
zbior_napisow = {'abc', 'ala ma kota', 'Słowwacki był poeta', 'Superman'}
print({x:len(x) for x in zbior_napisow})

#--- podzielne przez 3 ----
print([x for x in range(1,101) if x%3==0])


