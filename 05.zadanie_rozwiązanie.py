plec = int(input("Podaj płeć (0 - chłopiec, 1 - dziewczyna):"))
wiek = int(input("Podaj wiek"))

#sposób 1:
if plec == 0: #chłopiec
    if 14 <= wiek <= 17:
        print("kwalifikujesz się")
    else:
        print("nie kwalifikujesz się")
else: #dziewczynka
    if 11 <= wiek <= 13:
        print("kwalifikujesz się")
    else:
        print("nie kwalifikujesz się")


#sposób 2:
if (plec == 0 and 14 <= wiek <= 17) or (plec == 1 and  11 <= wiek <= 13):
    print("kwalifikujesz się")
else:
    print("nie kwalifikujesz się")
    
print("Do widzenia")
