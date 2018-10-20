zbior = {1, 2, 3, 4}
print(zbior)
zbior.add(1)
zbior.add("a")

print(zbior)
print(1 in zbior)
# ----------------------

for i in zbior:
    print(i)
# ----------------------
a = {1,2,3}
b = {3,4,5}

print(a | b) # suma
print(a - b) # różnica
print(a & b) # część wspólna
print(a ^ b) # różnica symetryczna

# ----------------------
print(dir(a))
print(a.union(b))
print(a.difference(b))
print(a.intersection(b))
print(a.symmetric_difference(b))

# ----------------------
print(set([12,3,4,5]))
print(set(range(1,10)))