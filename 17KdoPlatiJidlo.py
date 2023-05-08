import random
names = input("Napiš jména všech zůčastněných, odděl je čárkou.\n")
list_names = names.split(", " and ",")
random_number = random.randint(0, len(list_names)-1)
print(f"Si smolař a platíš {list_names[random_number]}")


# Druhá jednodušší mžonost
# print(f"Si smolař a platíš {random.choice(list_names)}")
