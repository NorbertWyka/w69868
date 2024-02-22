def zmien_wielkosc(litera):
    if litera.islower():
        return litera.upper()
    elif litera.isupper():
        return litera.lower()
    else:
        return litera

litera_poczatkowa = input("Podaj literę: ")
wynik = zmien_wielkosc(litera_poczatkowa)
print("Litera po zamianie: ", wynik)