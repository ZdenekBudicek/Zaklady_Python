height = input("Zadejte svou výšku v metrech:\n")
weight = input("Zadejte svou váhu v kg:\n")
bmi = int(weight) / float(height)**2
bmi = round(bmi, 1)
if bmi < 18.5:
    print(f"Vaše BMI je: {bmi}\nMáte podváhu, měl/a by jste konečně začít pořádně papat. :)")
elif bmi < 25:
    print(f"Vaše BMI je: {bmi}\nVaše váha je naprosto v pořádku.")
elif bmi < 30:
    print(f"Vaše BMI je: {bmi}\nMáte nadváhu, trošku uber stehýnek a všechno bude v pohodě.")
elif bmi < 35:
    print(f"Vaše BMI je: {bmi}\nJste obézní, ale ještě to půjde zachránit.")
else:
    print(f"Vaše BMI je: {bmi}\nTady už to nemá smysl, jen papej.")
