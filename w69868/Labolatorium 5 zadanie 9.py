import random

def podany_przedział(dolny_przedzial, gorny_przedzial):
    return dolny_przedzial < gorny_przedzial

def zgadywana_liczba(zgadywana, dolny_przedzial, gorny_przedzial):
    return dolny_przedzial <= zgadywana <= gorny_przedzial
try:
    dolny_przedzial = int(input("Podaj dolny zakres liczb:"))
    gorny_przedzial = int(input("Podaj górny zakres liczb:"))

    if not podany_przedział(dolny_przedzial, gorny_przedzial):
        print("Podajno niepoprawny zakres liczb")
    else:
        ukryta_liczba = random.randint(dolny_przedzial, gorny_przedzial)
        proby = 3

        while proby > 0:
            zgadywana =input("Zgadnij liczbę z podanego zakresu")
            if not zgadywana.isdigit() or not zgadywana_liczba(int(zgadywana), dolny_przedzial, gorny_przedzial):
                print("Podajno niepoprawną liczbę, Podaj liczbę z zakresu")
                continue

            zgadywana = int(zgadywana)
            if zgadywana == ukryta_liczba:
                print("Brawo! Zgadłeś liczbę")
            elif  zgadywana < ukryta_liczba:
                print("Podana liczba jest za mała")
            else:
                print("Podana liczba jest za duża")

            proby = proby - 1
            if proby > 0:
                print("Pozostało prób:", proby)
            else:
             print("Niestedty nie udało ci się, Zgadywana liczba to:", ukryta_liczba)

except ValueError:
    print("Podano nieprawidłową wartość. Upewnij się, że podane wartości są liczbami całkowitymi.")
