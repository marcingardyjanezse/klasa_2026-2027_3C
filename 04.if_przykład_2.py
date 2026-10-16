print("Podaj liczbę:")
a = int(input())

#jeden się wykona
if a > 5 and a < 10:
    print("Sekcja 1")
elif a >= 6 and a < 20:
    print("Sekcja 2")
else:
    print("Sekcja 3")

#każdy niezalżnie może zajść lub nie
if a > 5 and a < 10:
    print("Sekcja 1")
if a >= 6 and a < 20:
    print("Sekcja 2")


print("Do widzenia")
