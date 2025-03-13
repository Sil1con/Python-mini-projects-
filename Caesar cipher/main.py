# DAY 8

## Prime and composite numbers
# def prime_checker(number):
#   a = []
#   f = 2
#   while number > 1:
#     if number % f == 0:
#       a.append(f)
#       number //= f
#     else:
#       f += 1
#   if len(a) == 1:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")

## Caesar Cipher
# from art import logo
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# stop = False

# def caesar(text, shift, mode):
#     word = ""
#     def encrypt(text, shift):
#             encoded_word = ""
#             for letter in text:
#                 if letter in alphabet:
#                     index = alphabet.index(letter) + shift
#                     if index < len(alphabet):
#                         while index < len(alphabet):
#                             index += len(alphabet)
#                     if index >= len(alphabet):
#                         while index >= len(alphabet):
#                             index -= len(alphabet)
#                     encoded_word += alphabet[index]
#                 else:
#                     encoded_word += letter
#             return encoded_word

#     if mode == "encode": 
#         word = encrypt(text, shift)
#         print(f"Your encrypted message: {word}")
#     elif mode == "decode":
#         shift *= -1
#         word = encrypt(text, shift)
#         print(f"Your decrypted message: {word}")
#     else:
#         print("Choose 'encode' or 'decode'!")

# print(logo + "\n\n")
# while stop == False:
#     mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number: "))
#     caesar(text, shift, mode)

#     repeat = input("Would you like to continue: 'yes' or 'no'\n")
#     if repeat == "no":
#         stop = True