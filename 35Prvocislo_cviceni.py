# Prvočísla
# user_number = int(input("Zadejte jakékoli celé číslo: "))
# for one_number in range(2, user_number):
#     result = user_number % one_number
#     if result == 0:
#         print("Není to prvočíslo.")
#         break
# else:
#     print("Je to prvočíslo")


# Prvočíslo
def prime_number_checker(number):
    result = "Je to prvočíslo"
    for one_number in range(2, number):
        if number % one_number == 0:
            result = "Není to prvočíslo"
    print(result)


n = int(input("Zadejte prosím číslo: "))
prime_number_checker(n)
