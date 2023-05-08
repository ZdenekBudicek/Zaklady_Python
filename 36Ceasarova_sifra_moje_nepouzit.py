import itertools

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
sifra = []
sifra2 = []


def want(t):
    if t == "encode":
        message = input("Type your message:\n").lower()

        shift = int(input("type your shift number:\n"))
        for index in range(0, len(message)):
            for index2 in range(0, len(alphabet)):
                if message[index] == alphabet[index2]:
                    numero = index2 + shift
                    while numero > 25:
                        numero -= len(alphabet)
                    sifra.append(alphabet[numero])
                    zmena = "".join(map(str, sifra))
        print(f"Encrypted text is: {zmena}")
    elif t == "decode":
        message2 = input("Type your message:\n").lower()
        shift2 = int(input("Type the shift number:\n"))
        for index in range(0, len(message2)):
            for index2 in range(0, len(alphabet)):
                if message2[index] == alphabet[index2]:
                    desifra = index2
                    desifra = index2 - shift2
                    while desifra < 0:
                        desifra += len(alphabet)
                    sifra2.append(alphabet[desifra])
                    zmena2 = "".join(map(str, sifra2))
        print(f"Encrypted text is: {zmena2}")
        pokracovat = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    else:
        print("Neotravuj když neumíš psát!")


want(input("Type 'encode' to enrypt, type 'decode' to decrypt\n").lower())
