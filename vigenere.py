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

for i in ptxt:

    key = key_list[kpos]

    if i.isupper():
        char = chr((ord(i) + key) % 91)

        if char < chr(65):
            char = chr(ord(char) + 65)

        print(char, end = "")




    elif i.islower():
        char = chr((ord(i) + key) % 123)
        if char < 'a':
            char = chr(ord(char) + 97)
        print(char, end = "")
    else:
        print(i, end = "")

    kpos += 1
    if kpos > len(key_word) - 1:
        kpos = 0
print("")






