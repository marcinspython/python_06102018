x = int(input("Podaj pozycję X "))
y = int(input("Podaj pozycję Y "))

if x>100 or y > 100 or x < 0 or y <0:
    print("Wypadłeś z planszy")
elif x>90 and y > 90:
    print("Jesteś w prawym górnym rogu")
elif x > 90 and y <10:
    print("jestes w prawym dolnym rogu")
elif x < 100 and y <10:
    print("jestes w prawym dolnym rogu")
elif x < 10 and y <90:
    print("jestes w prawym dolnym rogu")
elif x < 10:
    print("lewa krawedz")
elif x > 90:
    print("prawa krawedz")
elif y < 10:
    print("dolna krawedz")
elif y > 90:
    print("dolna krawedz")
else:
    print("jesteś w centrum")

    # 222 ddddddddddddddd

    x = int(input("Podaj pozycję X "))
    y = int(input("Podaj pozycję Y "))

    wym_x = int(input("Podaj pozycję X "))
    wym_y = int(input("Podaj pozycję Y "))

    if x > 100 or y > 100 or x < 0 or y < 0:
        print("Wypadłeś z planszy")
    elif x > 90 and y > 90:
        print("Jesteś w prawym górnym rogu")
    elif x > 90 and y < 10:
        print("jestes w prawym dolnym rogu")
    elif x < 100 and y < 10:
        print("jestes w prawym dolnym rogu")
    elif x < 10 and y < 90:
        print("jestes w prawym dolnym rogu")
    elif x < 10:
        print("lewa krawedz")
    elif x > 90:
        print("prawa krawedz")
    elif y < 10:
        print("dolna krawedz")
    elif y > 90:
        print("dolna krawedz")
    else:
        print("jesteś w centrum")