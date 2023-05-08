year = int(input("Vyberte si rok a zjistěte zda je přestupný či nikoliv\n"))
if year % 4 == 0:
    if year % 100 != 0:
        print("Přestupný rok")
    elif year % 400 == 0:
        print("Je to přestupný rok.")
    else:
        print("Není to přestupný rok.")
else:
    print("Není to přestupný rok")
