import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

number_of_letters = []
number_of_numbers = []
number_of_special_symbols = []
all_values = []
list_of_letters = []

print("Vítejte v generátoru hesel.")
user_letters = int(input("Kolik chcete aby vaše heslo mělo písmen?\n"))
user_numbers = int(input("Kolik chcete aby vaše heslo mělo čísel?\n"))
user_special_symbols = int(input("Kolik chcete aby vaše heslo mělo speciálních znaků?\n"))

random_letters = random.choices(letters, weights=None, cum_weights=None, k=user_letters)
for indexl in range(0, len(random_letters)):
    number_of_letters.append(random_letters[indexl])
string_letters = ''.join(map(str, number_of_letters))

random_number = random.choices(numbers, weights=None, cum_weights=None, k=user_numbers)
for indexN in range(0, len(random_number)):
    number_of_numbers.append(random_number[indexN])
string_numbers = ''.join(map(str, number_of_numbers))

random_special_symbol = random.choices(special_char, weights=None, cum_weights=None, k=user_special_symbols)
for indexs in range(0, len(random_special_symbol)):
    number_of_special_symbols.append(random_special_symbol[indexs])
string_special_symbols = ''.join(map(str, number_of_special_symbols))

all_values.append(string_letters + string_numbers + string_special_symbols)
string_all_values = ''.join(map(str, all_values))
for one_letter in string_all_values:
    list_of_letters.append(one_letter)
random.shuffle(list_of_letters)
letters_string = "".join(map(str, list_of_letters))
print(letters_string)
