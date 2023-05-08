import random
from Data_Higher_lower import data


def game():
    global generate
    global generate2
    generate = random.choice(data)
    generate2 = random.choice(data)
    while generate == generate2:
        generate2 = random.choice(data)
    global guess
    guess = input("Co je více A) " + generate["name"] + " " + "nebo" + " B) " + generate2[
        "name"] + " " + "napište A nebo B:\n").lower()
    if generate["follower_count"] > generate2["follower_count"]:
        if guess == "a":
            return True
        else:
            print("Špatně, možnost A byla správně")
    elif generate["follower_count"] < generate2["follower_count"]:
        if guess == "b":
            return True
        else:
            print(f"Špatně, možnost B byla správně")
    else:
        print("draw")


result = game()
print(result)
print(guess)


def again():
    while result == True:
        global guess
        global generate
        global generate2
        print(guess)
        if guess == "a":
            generate2 = random.choice(data)
            guess = input("Co je více A) " + generate["name"] + " " + "nebo" + " B) " + generate2[
                "name"] + " " + "napište A nebo B:\n").lower()
            if generate["follower_count"] > generate2["follower_count"]:
                if guess == "a":
                    return True
                else:
                    print("Špatně, možnost A byla správně")
            elif generate["follower_count"] < generate2["follower_count"]:
                if guess == "b":
                    return True
                else:
                    print(f"Špatně, možnost B byla správně")
            else:
                print("draw")
        if guess == "b":
            generate = random.choice(data)
            guess = input("Co je více A) " + generate2["name"] + " " + "nebo" + " B) " + generate[
                "name"] + " " + "napište A nebo B:\n").lower()
            if generate2["follower_count"] > generate["follower_count"]:
                if guess == "a":
                    return True
                else:
                    print("Špatně, možnost A byla správně")
            elif generate2["follower_count"] < generate["follower_count"]:
                if guess == "b":
                    return True
                else:
                    print(f"Špatně, možnost B byla správně")
            else:
                print("draw")


result = again()
