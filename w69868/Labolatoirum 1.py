pada_deszcz = input("Czy pada deszcz? (Tak/Nie): ") == 'tak'
jest_autobus = input("Czy jest autobus na przystanku? (Tak/Nie): ") == 'tak'

if pada_deszcz and jest_autobus:
    print("Weź parasol")
    print("Dostaniesz się na uczelnię")
elif pada_deszcz and not jest_autobus:
    print("Nie dostaniesz się na uczelnię")
elif not pada_deszcz and jest_autobus:
    print("Dostaniesz się na uczelnię")
    print("Miłego dnia i pięknej pogody")
else:
    print("Nie dostaniesz się na uczelnie, ale jest piękna pogoda")