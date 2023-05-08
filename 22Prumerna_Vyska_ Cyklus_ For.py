user = (input("Vložte výšky lidí oddělené čárkou a mezerou:\n"))
amount = 0
split = user.split(", ")
number = len(split)
for one_height in split:
    amount = amount + int(one_height)
average = amount / number
print(f"Průměrná výška je: {average}")
