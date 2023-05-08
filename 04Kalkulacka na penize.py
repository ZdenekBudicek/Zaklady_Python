print("Vítejte v kalkulačce na výpočet plateb")
overall = int(input("Kolik máte celkem zaplatit?\n"))
tip = int(input("Kolik chcete dát spropitného (v %)?\n"))
people = float(input("Mezi kolik lidí se má rozdělit částka?\n"))
every_person = (overall + (overall * tip / 100)) / people
print(f"Každý člověk by měl zaplatit {'{:.2f}'.format(every_person)} Kč.")
