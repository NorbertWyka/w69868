n = int(input("Podaj liczbę studentów w grupie"))
liczba = 0
suma_punktow = 0

while   liczba < n:
    punkty = float(input("Podaj Liczbę punktów dla studneta "))
    suma_punktow += punkty
    liczba += 1

srednia_punktow = suma_punktow/n
print("Suma punktów wynosi", srednia_punktow)
