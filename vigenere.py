from sys import argv
from cs50 import get_string

#Check if the arguments are okay
if len(argv) != 2 or not argv[1].isalpha():
    exit("Usage: python vigenere.py key")

key_word = argv[1].upper()
key_list = []

for c in key_word:
    num = int(ord(c) - 65)
    key_list.append(num)

print (key_list)
ptxt = get_string("plaintext: ")
print("ciphertext: ", end = "")
kpos = 0

for char in ptxt:

    key = key_list[kpos]

    if char.isupper():
        char = chr(ord(char) + key)
        if char > 'Z':
            char = chr(ord(char) + 65)
        kpos += 1


    elif char.islower():
        char = chr(ord(char) + key)
        if char > 'z':
            char = chr(ord(char) + 97)
        kpos += 1

    print(char, end = "")



    if kpos > len(key_word) - 1:
        kpos = 0

print("")






