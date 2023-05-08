import random

player = int(input("Kámen, nůžky, papír teď. Co si zvolíte?: (Kámen = 1, Papír = 2, nůžky = 3)\n"))
if player > 3:
    print("Zkus to znovu")
elif player <= 0:
    print("Zkus to znovu")
else:
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    game = [rock, paper, scissors]
    print(f"Zvolil sis: {game[player - 1]}")
    number = random.randint(0, 2)
    print(f"Tvůj protihráč zvolil:\n{game[number]}")
    # Kámen
    if player == 1 and number == 2:
        print("Gratuluji, vyhrál jsi, jsi opravdodvý šampion!")
    elif player == 1 and number == 1:
        print("Smůla, dostal jsi na frak!\nZkus znovu své štěstí.")
    elif player == 1 and number == 0:
        print("Máme tady remízu!\nMusíme to rozhodnout, pojď jetě jednou.")
        # Papír
    if player == 2 and number == 2:
        print("Smůla, dostal jsi na frak!\nZkus znovu své štěstí.")
    elif player == 2 and number == 1:
        print("Máme tady remízu!\nMusíme to rozhodnout, pojď jetě jednou.")
    elif player == 2 and number == 0:
        print("Gratuluji, vyhrál jsi, jsi opravdodvý šampion!")
        # Nůžky
    elif player == 3 and number == 2:
        print("Máme tady remízu!\nMusíme to rozhodnout, pojď jetě jednou.")
    elif player == 3 and number == 1:
        print("Gratuluji, vyhrál jsi, jsi opravdodvý šampion!")
    elif player == 3 and number == 0:
        print("Smůla, dostal jsi na frak!\nZkus znovu své štěstí.")
