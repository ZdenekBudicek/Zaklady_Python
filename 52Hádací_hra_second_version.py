import random
import os
from logo_hádací_hra import logo

# Úvodní informace
print(logo)
print("Vítejte ve hře guess secret number. Porazte počítač.")
print("Myslím si číslo od 1 do 100")

# Příprava hry
secret_number = random.randint(1, 100)
print(f"Hádané číslo je {secret_number}")


def difficulty():
    difficulty = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5


# Počet pokusů
def guessing_game():
    attemps = difficulty()

    another_game = ""

    while attemps > 0:
        print(f"Váš počet zbývajících pokusů je {attemps}")
        guess = int(input("Typněte si číslo: "))

        if guess < secret_number:
            print("Příliš nízké")
            attemps -= 1
        elif guess > secret_number:
            print("Příliš vysoké")
            attemps -= 1
        else:
            print("Vyhráli jste. Počítač poražen!")
            another_game = input("Napište 'yes', pokud chcete pokračovat. Napište 'no', pokud chcete hru ukončit")

        if attemps == 0:
            print("Prohráli jste. Počítač vyhrál!")
            another_game = input("Napište 'yes', pokud chcete pokračovat. Napište 'no', pokud chcete hru ukončit")

        if another_game == "yes":
            os.system("cls")
            guessing_game()
        elif another_game == "no":
            os.system("cls")
            break


guessing_game()
