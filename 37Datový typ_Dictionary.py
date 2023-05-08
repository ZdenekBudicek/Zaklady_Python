it_dictionary = {
    "Integer": "Celé číslo",
    "String": "Text",
    "Float": "Desetinné číslo",
    "Boolean": "Pravda nepravda"
}

print(it_dictionary["String"])
print(it_dictionary["Integer"])
print(it_dictionary["Boolean"])

it_dictionary_2 = {
    1: "Text",
    2: "Desetinné číslo",
    0: "Celé číslo",
    3: "Pravda nepravda"
}
print(it_dictionary_2)
print(it_dictionary_2[0])
print(it_dictionary_2[1])
print(it_dictionary_2[2])

# Přidání hodnot do dictionary
it_dictionary_2[4] = "Uložení více hodnot"
print(it_dictionary_2)

# Nastavení prázdného dictionary
empty_dictionary = {}

# Vyprázdnit dictionary
it_dictionary_2 = {}

# Měníme hodnoty v dictionary
it_dictionary_2[1] = "Textová hodnota"
print(it_dictionary_2)
