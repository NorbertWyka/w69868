def czy_anagram(slowo1, slowo2):
    return sorted(slowo1) == sorted(slowo2)


slowo1 = input("Podaj pierwsze słowo(małymi literami)")
slowo2 = input("Podaj drugie słowo(małymi literami")

if czy_anagram(slowo1, slowo2):
    print("Podane słowa są anagramami")
else:
    print("Podane słowa nie są anagramami")