from auction_logo import auction_logo
import os

print(f"{auction_logo}\n\n Vítejte v programu pro tichou dražbu.")

# Naplnění dictionary nabízejícími
dictionary = {}
decision = "ano"
while decision == "ano":
    name = input("Jaké je vaše jmeno?\n")
    cash = int(input("Jaká je vaše nabídka v dolarech?\n"))
    dictionary[name] = cash
    decision = input("Jsou další nabízející? Napište 'ano' nebo 'ne'.\n")
    if decision == "ne":
        os.system("cls")

# Hledání nejvyšší nabídky
hodnota = 0
winner = ""
for key in dictionary:
    if hodnota < dictionary[key]:
        hodnota = dictionary[key]
        winner = key
print(f"Vítězem tiché aukce je: {winner} s částkou {hodnota} dolarů.")
