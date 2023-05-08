# funkce a return

# def sum(number1, number2):
#     print(number1 + number2)
#
#
# sum(5, 20)
#
#
# def better_name(first_name, second_name):
#     first_name = first_name.capitalize()
#     second_name = second_name.capitalize()
#     return f"{first_name} {second_name}"


def better_name(first_name, second_name):
    full_name = first_name + " " + second_name
    return full_name.title()


result = better_name("Zdeněk", "NĚKDO")
print(result)
