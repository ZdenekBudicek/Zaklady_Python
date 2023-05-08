print("Vítejte na horské dráze.")
height = int(input("Jaká je vaše výška v cm?\n"))
price = 0
if height >= 87:
    print("Můžete jet na horské dráze")
    age = int(input("Jaký je váš věk?\n"))
    if age < 12:
        price = 80
        print("Cena vašeho lístku je 80 Kč")
    elif age < 18:
        price = 140
        print("Cena vašeho lístku je 140 Kč")
    elif 50 <= age <= 60:
        print("Jste šťastlivec a jedete ZDARMA!")
    else:
        print("Cena vašeho lístku je 180 Kč")
        price = 180
    photo = input("Chcete se nechat vyfotit?\n")
    if photo == "ano":
        price += 40
        print(f"Celkem je vaše cena {price} Kč.")
    else:
        print(f"Vaše cena je stále {price} Kč")
else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")

