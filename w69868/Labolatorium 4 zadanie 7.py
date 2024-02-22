def czy_palindrom(slowo):
    return slowo == slowo[::-1]

slowo = input("Podaj słowo małymi literami: ")
if czy_palindrom(slowo):
    print("To słowo jest palindromem.")
else:
    print("To słowo nie jest palindromem.")