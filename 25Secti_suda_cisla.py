# Složitě

# even_number = []
# number = 0
# for one_number in range(1, 101):
#     if one_number % 2 == 0:
#         even_number.append(one_number)
# for one_even_number in even_number:
#     number = number + one_even_number
# print(number)

# Jednoduše

number = 0
for even_number in range(0, 101, 2):
    number += even_number
print(number)
