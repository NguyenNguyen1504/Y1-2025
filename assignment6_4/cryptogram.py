import random
from sys import orig_argv

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SENTENCES = [
    "I am on my way to see you.",
    "You are in the big blue house.",
    "The sun is up, and I am happy.",
    "A cat is in the box with a toy.",
    "My dog is on the bed asleep.",
    "We go to the park for a walk.",
    "She is at home with her cat.",
    "The boy is by the tall tree.",
    "I have a pen and a pad for notes.",
    "You and I are on a fun trip.",
]

def create_cipher(text):
    text_alphabet = []
    for letter in ALPHABET:
        if letter in text:
            text_alphabet.append(letter)
    text_alphabet_shuffled = text_alphabet.copy()
    random.shuffle(text_alphabet_shuffled)
    # create and return the encryption/decryption key here
    encrypt = {}
    decrypt = {}
    for i in range (len(text_alphabet)):
        original = text_alphabet[i]
        shuffled = text_alphabet_shuffled[i]
        encrypt[original] = shuffled
        decrypt[shuffled] = original
    return encrypt, decrypt

# write the remaining functions here
def apply_cipher(text, cipher):
    ciphered_text = ""
    for letter in text:
        if letter in cipher:
            ciphered_text += cipher[letter]
        elif letter in ALPHABET:
            ciphered_text += '_'
        else:
            ciphered_text += letter
    return ciphered_text


def guess_input(reverse_cipher, found_cipher):
    user_encr = ""
    while user_encr == "":
        user_encr = input("Guess the letter in the shuffled text:\n").upper()
        if user_encr in found_cipher:
            print(f"You already correctly guessed '{user_encr}'.")
        elif user_encr not in reverse_cipher:
            print(f"'{user_encr}' is not in the cryptogram.")
        else:
            user_encr = user_encr
    user_decr = input(f"What does '{user_encr}' map to:\n").upper()
    return user_encr, user_decr


def print_progress(shuffled_text, found_cipher):
    print()
    print(f"Shuffled: {shuffled_text}")
    print(f"Progress: {apply_cipher(shuffled_text, found_cipher)}")
    print()

def main():
    random.seed(int(input("Set the seed:\n")))
    original_text = random.choice(SENTENCES).upper()
    # write the main program here
    cipher, reverse_cipher = create_cipher(original_text)
    found_cipher = {}
    shuffled_text = apply_cipher(original_text, cipher)

    while len(cipher) != len(found_cipher):

        print_progress(shuffled_text, found_cipher)

        user_encr, user_decr = guess_input(reverse_cipher, found_cipher)
        correct_letter = reverse_cipher[user_encr]
        if user_encr == correct_letter:
            print(f"Correct! '{user_encr}' is '{user_decr}'.")
            found_cipher[user_encr] = correct_letter
        else:
            print(f"Incorrect. '{user_encr}' is not '{user_decr}'.")

    print("You solved the cryptogram!")
    print_progress(shuffled_text, found_cipher)


main()