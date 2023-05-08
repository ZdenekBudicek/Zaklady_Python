age = int(input("Kolik vám je let?\n"))
years = 90 - age
months = years * 12
weeks = years * (365 / 7)
days = 365 * years
print(
    f"Zůstává vám  {years} let života.\nZůstává vám {months} měsíců života.\n"
    f"Zůstává vám {round(weeks)} týdnů života.\nZůstává vám {days} dnů života.")
