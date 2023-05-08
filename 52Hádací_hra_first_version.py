import random
import os

from logo_hádací_hra import logo

print(f"{logo}\nVítejte ve hře Guess Secret Number. Poraz protihráče!\nMyslím si číslo od 1 do 100.")


def game():
    lives = 0
    difficult = input("Vyberte si obtížnost, napište 'EASY' nebo 'HARD':\n").lower()
    number = random.randint(1, 100)
    if difficult == "easy":
        lives += 10
    elif difficult == "hard":
        lives += 5
    else:
        print("Chybná odpověď, zkus to znovu")
        game()

    # Hádání čísla
    guess = 0
    while guess != number and lives != 0:
        guess = int(input("Tipněte si číslo:\n"))
        if guess > number:
            lives -= 1
            print("Příliš vysoké")
            print(f"Váš počet zbývajících životů je: {lives}")
        elif guess < number:
            lives -= 1
            print("Příliš nízké")
            print(f"Váš počet zbývajících životů je: {lives}")
        else:
            print(f"Vyhrál jsi, gratuluji šampione! Hádané číslo bylo skutečně {guess}.")
        if lives == 0:
            print(f"Prohrál jsi, hádané číslo bylo {number}")
    again = ""
    while again != "yes" and again != "no":
        again = input("Napište 'YES', pokud chcete pokračovat. Napište 'NO', pokud chcete hru ukončit:\n").lower()
        if again == "yes":
            os.system("cls")
            game()
        elif again == 'no':
            os.system("cls")
        else:
            print("Chybná odpověď, zkus to znovu")


game()
