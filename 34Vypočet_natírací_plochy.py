# jedna plechovka 5m
import math

print("Vítejte v kalkulačce na natírání ploch.\n")
height = float(input("Výška zdi: "))
width = float(input("Šířka zdi: "))


def colors(number):
    result = number / 5
    if result <= 1:
        print(f"Potřebujete {math.ceil(result)} plechovku barvy")
    elif 1 < result <= 4:
        print(f"Potřebujete {math.ceil(result)} plechovky barvy")
    else:
        print(f"Potřebujete {math.ceil(result)} plechovek barvy")


colors(height * width)
