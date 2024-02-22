szerokosc = 6
wysokosc = 5

przeciwnicy = [(0, 1), (2, 3), (2,4), (3, 4)]
monety = [(1, 1), (2, 0), (3, 3), (5, 3)]

rzeka_y = 2

for y in range(wysokosc):
    for x in range(szerokosc):
        if (x, y) in przeciwnicy:
            print("x", end = '')
        elif (x, y) in monety:
            print("*", end = '')
        elif y == rzeka_y:
            print("=", end = '')
        else:
            print("-", end = '')
    print()

