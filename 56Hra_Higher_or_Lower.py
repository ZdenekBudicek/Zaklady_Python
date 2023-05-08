from Data_Higher_lower import data
import random


def printing_options(acc1, acc2):
    print(f"Porovnejte A: {acc1['name']}, {acc1['description']}, {acc1['country']}")
    print(f"Porovnejte B: {acc2['name']}, {acc2['description']}, {acc2['country']}")


def game():
    account_1 = random.choice(data)
    account_2 = random.choice(data)
    while account_1 == account_2:
        account_2 = random.choice(data)
    right_answer = ""
    score = 0
    lets_continue = True

    while lets_continue:
        # Pro testovací účely

        # print(f"Testovací výpis - účet 1: {account_1['follower_count']}")
        # print(f"Testovací výpis - účet 2: {account_2['follower_count']}")

        printing_options(account_1, account_2)

        user_answer = input("Kdo má více sledujících na instagramu? Napište A nebo B. ").lower()
        if account_1["follower_count"] > account_2["follower_count"]:
            right_answer = "a"
        else:
            right_answer = "b"

        if right_answer == user_answer:
            score += 1
            print(f"Uhádli jste. Vaše skóre je {score}")
            account_1 = account_2
            account_2 = random.choice(data)
            while account_1 == account_2:
                account_2 = random.choice(data)
        else:
            print(f"To je špatně. Vaše konečné skóre je {score}")
            lets_continue = False


game()
