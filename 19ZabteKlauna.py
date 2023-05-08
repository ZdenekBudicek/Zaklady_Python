import random
set1 = ["🤠", "🥶", "☠️", "👻"]
set2 = ["🧐", "👻", "🤡", "💩"]
set3 = ["👽", "🤖", "🥵", "👀"]
set4 = ["🧐", "🤕", "🏐", "🐗"]
set5 = ["🦚", "😎", "🐏", "👻"]
set6 = ["🦞", "🤖", "🐏", "😱"]
set7 = ["🕸", "⚽️", "🏐", "👻"]
random.shuffle(set1 + set2 + set3 + set4 + set5 + set6 + set7)
all_sets = [set1, set2, set3, set4, set5, set6, set7]
random.shuffle(all_sets)
print(all_sets[0])
print(all_sets[1])
print(all_sets[2])
print(all_sets[3])
print(all_sets[4])
print(all_sets[5])
print(all_sets[6])
print("Vítejte ve hře Zabte klauna")
position = input("Zadejte souřadnice (0 až 6 a 0 až 3) a oddělte je čárkou. Váš úkol je zabít klauna!\n")
split = position.split(", " and ",")
position1 = int(split[0])
if position1 > 6:
    print("Zadal si špatnou hodnotu, koukej to napravit!")
else:
    position2 = int(split[1])
    if position2 > 3:
        print("Zadal si špatnou hodnotu, koukej to napravit!")
    else:
        all_sets[position1][position2] = "❌"
        print(all_sets[0])
        print(all_sets[1])
        print(all_sets[2])
        print(all_sets[3])
        print(all_sets[4])
        print(all_sets[5])
        print(all_sets[6])
