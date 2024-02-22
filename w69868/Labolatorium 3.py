import random

while True:
    cyfry = input("Podaj pięć cyfr odzielone przeninkami:")
    cyfry = cyfry.split(',')
    if len(cyfry) !=5:
        print("Podano złą ilośc cyfr")
    else:
        break

cyfry = set(map(int, cyfry))

wylosowana_liczba = random.choice(list(cyfry))
if wylosowana_liczba == min(cyfry):
    print(f"Wylosowana liczba {wylosowana_liczba} jest najmniejszą z podanych liczb.")
elif wylosowana_liczba == max(cyfry):
    print(f"Wylosowana liczba {wylosowana_liczba} jest największą z podanych liczb.")
else:
    print(f"Wylosowana liczba {wylosowana_liczba} nie jest ani największą, ani najmniejszą z podanych liczb.")