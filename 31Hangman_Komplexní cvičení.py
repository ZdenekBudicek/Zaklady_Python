import random
from Obrazky_k_Hangman import stages

# Generovat random slovo
words = "pilulka | měsíc | poustevník | nálet | dobytek | štětec | úpal | nos | kvintet | listina | chrám | lebka | kužel | vada | roleta | pramínek | poučení | prodlužovák | kometa | koberec | linka | pouto | kov | kůzlátko | věc | instalatér | průliv | podchod | korupce | vrtulník | kouzelnice | improvizace | nemčina | půllitr | zákusek | ropa | vysavač | vlajka | nemocnice | hospoda | hrudka | hadička | kry | kukačka | sardinka | omluva | rohožka | trojúhelník | sušák | obchod | bod | malba | úl | bodec | slot | album | bitka | pásmo | úsvit | účel | karanténa | prostor | programátor | řezník | čich | úval | místo | hrůza | hříbek | náskok | sněm | hněv | kondom | proces | zátiší | bruska | pilník | lokomotiva | přikrývka | večer | tvář | krápník | akustika | zrcadlo | kapka | vzducholoď | hřebec | flek | síla | podobnost | pohovka | žehlička | protekce | silonky | odvaha | introvert | bazilika | inflace | barel | ředitel"
words_list = words.split(" | ")
random_word = words_list[random.randint(0, len(words_list) - 1)]

# random_word = random.choice(words_list)
# print(random_word)

# Generování podtržítek
hidden_word = []
for one_letter in random_word:
    hidden_word.append(" _")

# Životy
lives = 8
print(stages[lives])

# Vypsání slova s podtržítky v normální podobě
printed_word = ""
for one_letter in hidden_word:
    printed_word += one_letter
print(printed_word)

# Hádání
while " _" in hidden_word:
    guess = input("Zadejte hádané písmeno\n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess

    # Kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    print(f"Počet vašich životů je {lives}")
    if lives == 0:
        print(f"Prohráli jste, hledané slovo bylo '{random_word}'")

        break

    # Vypsání slova s podtržítky v normální podobě
    printed_word = ""
    for one_letter in hidden_word:
        printed_word += one_letter
    print(printed_word)

    # Kontrola vítězství
    if " _" not in hidden_word:
        print("Vyhráli jste!!!")
