from sys import argv
from cs50 import get_string

#Check if the arguments are okay
if len(argv) != 2 or not argv[1].isalpha():
    exit("Usage: python vigenere.py key")



list_k = argv[1].upper()
nums = []
for c in list_k:
    char = ord(c) - 65
    print (c)
    nums.append(char)
print(nums[0])