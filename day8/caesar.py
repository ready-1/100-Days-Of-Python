# This is not a polished app.  It still needs some input validation
# and a clean front end.  This project is meant to show list manipulation.
# There is a need to refactor to combine the encode & decode functions into
# one function with some logic to manage the character pools.

from os import system, name
from string import ascii_letters, digits, punctuation, whitespace


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def is_valid_char(char, pool):
    # check to see if the character is in our pool
    if char in pool:
        return True
    else:
        return False


def encode(plain_text, shift):
    # make a list of all the characters and whitespace
    plain_pool = make_plain_pool()
    # make a list that has the shift applied
    cipher_pool = apply_shift(shift, plain_pool)
    # empty string to hold the encrypted text
    cipher_text = ""
    # do the encryption
    for plain_char in plain_text:
        if is_valid_char(plain_char, plain_pool):
            # get the index of the current unencrypted character in the plain text pool
            plain_index = plain_pool.index(plain_char)
            # use the plain text pool index to find the corresponding character from the cipher pool
            cipher_char = cipher_pool[plain_index]
            # add the encrypted character to the encrypted text to be returned
            cipher_text += cipher_char

    # return the encrypted text as a string
    return cipher_text


def decode(cipher_text, shift):
    # make a list of all the characters and whitespace
    plain_pool = make_plain_pool()
    # make a list that has the shift applied
    cipher_pool = apply_shift(shift, plain_pool)
    # empty string to hold the decrypted text
    plain_text = ""
    # do the decryption
    for cipher_char in cipher_text:
        if cipher_char in cipher_pool:
            # get the index of the current encrypted character in the cipher text pool
            cipher_index = cipher_pool.index(cipher_char)
            # use the cipher text pool index to find the corresponding character from the plain pool
            plain_char = plain_pool[cipher_index]
            # add decrypted character to the decrypted text to be returned
            plain_text += plain_char

    # return the unencrypted text as a string
    return plain_text


def make_plain_pool():
    return ascii_letters + digits + punctuation


def apply_shift(shift, unshifted):
    # get the character to shift to the upper end of the cipher pool
    upper_chars = unshifted[0:shift]
    # get the characters to shift to the lower end of the cipher pool
    lower_chars = unshifted[shift::]
    # combine the two pools of characters
    shifted = lower_chars + upper_chars
    return shifted


def main():
    clear()
    shift = int(input("Enter the shift: "))
    operation = input("Ender 'encode' or 'decode': ")
    text = input("Enter the text: ")

    result = ""

    if operation == 'encode':
        result = encode(text, shift)
    else:
        result = decode(text, shift)

    print(result)

    print(input("<Enter> to continue..."))
