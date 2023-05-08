print('Vítejte v aplikaci "Vyber si svojí Pizzu"')
choose = input("Máte vybráno? ano/ne\n")
if choose == "ano":
    size = input("Jakou velikost pizzy si dáte? (velkou, střední, malou)\n")
    chilli_peppers = 0
    cheese = 15
    pizza = 0
    if size == "velkou":
        chilli_peppers = 30
        pizza = 200
        print(f"Cena velké pizzy je {pizza} Kč.")
    elif size == "střední":
        chilli_peppers = 25
        pizza = 150
        print(f"Cena za střední pizzu je {pizza} Kč.")
    elif size == "malou":
        chilli_peppers = 20
        pizza = 100
        print(f"Cena za malou pizzu je {pizza} Kč.")

    choose_chilli_peppers = input("Dáte si na pizzu feferonky? Ano/ne\n")
    if choose_chilli_peppers == "ano":
        print(f"Za feferonky připlatíte {chilli_peppers} Kč.")

        more_cheese = input("Dáte si sýr navíc? Ano/ne\n")
        if more_cheese == "ano":
            overall = pizza + chilli_peppers + cheese
            print(f"Za pizzu zaplatíte {overall} Kč.")
        else:
            overall = pizza + chilli_peppers
            print(f"Za pizzu zaplatíte {overall} Kč.")
    else:
        more_cheese = input("Dáte si na pizzu sýr navíc? Ano/ne\n")
        if more_cheese == "ano":
            overall = pizza + cheese
            print(f"Za pizzu zaplatíte {overall} Kč.")
        else:
            print(f"Za pizzu zaplatíte {pizza} Kč.")
else:
    print("Tak se rozmyslete a pak přijďte!")
