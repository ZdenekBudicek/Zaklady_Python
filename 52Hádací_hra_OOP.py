import random
import os

from logo_hádací_hra import logo


class Game:
    def __init__(self):
        self.lives = 0
        self.number = random.randint(1, 100)

    def set_difficulty(self, difficulty):
        if difficulty == "easy":
            self.lives += 10
        elif difficulty == "hard":
            self.lives += 5
        else:
            print("Chybná odpověď, zkus to znovu")
            self.set_difficulty(input("Vyberte si obtížnost, napište 'EASY' nebo 'HARD':\n").lower())

    def play(self):
        guess = 0
        while guess != self.number and self.lives != 0:
            guess = int(input("Tipněte si číslo:\n"))
            if guess > self.number:
                self.lives -= 1
                print("Příliš vysoké")
                print(f"Váš počet zbývajících životů je: {self.lives}")
            elif guess < self.number:
                self.lives -= 1
                print("Příliš nízké")
                print(f"Váš počet zbývajících životů je: {self.lives}")
            else:
                print(f"Vyhrál jsi, gratuluji šampione! Hádané číslo bylo skutečně {guess}.")
            if self.lives == 0:
                print(f"Prohrál jsi, hádané číslo bylo {self.number}")
        again = ""
        while again != "yes" and again != "no":
            again = input("Napište 'YES', pokud chcete pokračovat. Napište 'NO', pokud chcete hru ukončit:\n").lower()
            if again == "yes":
                os.system("cls")
                self.__init__()
                self.set_difficulty(input("Vyberte si obtížnost, napište 'EASY' nebo 'HARD':\n").lower())
            elif again == 'no':
                os.system("cls")
            else:
                print("Chybná odpověď, zkus to znovu")


print(f"{logo}\nVítejte ve hře Guess Secret Number. Poraz protihráče!\nMyslím si číslo od 1 do 100.")

game = Game()
game.set_difficulty(input("Vyberte si obtížnost, napište 'EASY' nebo 'HARD':\n").lower())
game.play()
