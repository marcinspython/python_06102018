#
# x=range(1, 500, 35) #przedział liczb z ilością znaków
# for i in x:
#     print(f'{i:7}', end='')
# print('costam')

# x = list(range(10))
# for i in x:
#     print(f'{i:7}', end='')
# # print(x)

# ########################################################

print("   ", end="")
for x in range(10):
# for x in range(1, 10):
    print(f"{x:3}", end=" ")
print()
print()

for x in range(10):
    print(x, end="  ")
    for y in range(10):
    # for y in range(1, 10):
        print(f"{x*y:3}", end=" ")
    print()
# ########################################################