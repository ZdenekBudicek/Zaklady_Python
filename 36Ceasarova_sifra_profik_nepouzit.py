alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(message, shift_number):
    shifted_text = ""
    for one_letter in message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index + shift_number
            shifted_text += alphabet[new_index]
        else:
            shifted_text += one_letter
    print(f"Your encrypted text is: {shifted_text}")


def decode(encrypted_message, shift_number):
    normal_text = ""
    for one_letter in encrypted_message:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            new_index = index - shift_number
            normal_text += alphabet[new_index]
        else:
            normal_text += one_letter
    print(f"Your decrypted text is: {normal_text}")


lets_continue = "yes"
while lets_continue == "yes":
    direction = input(
        "Napište 'encode', pokud chcete zakódovat zprávu. Napište 'decode', pokud chcete dekódovat zprávu.\n")
    text = input("Napište svou zprávu:\n").lower()
    shift = int(input("Napište hodnotu posunu:\n"))
    if direction == "encode":
        encode(text, shift)
        lets_continue = input(
            "Napište 'yes', pokud chcete pokračovat. Napište 'no', pokud chcete šifrovací program ukončit.")
    elif direction == "decode":
        decode(text, shift)
        lets_continue = input(
            "Napište 'yes', pokud chcete pokračovat. Napište 'no', pokud chcete šifrovací program ukončit.")
