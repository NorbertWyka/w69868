import random

liczby = list(range(1, 50))
liczby_loteri = random.sample(liczby, 6)
liczby_loteri.sort()
print(liczby_loteri)