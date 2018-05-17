import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

#word_format = "ccvcvvc"
word_format = input("Enter the word format in consonants and vowels only: ")
word_format.lower()
word = ""
for kind in word_format:
    if kind == "c" or kind=="%" or kind=="*":
        word += random.choice(CONSONANTS)
    elif kind=="v" or kind=="#":
        word += random.choice(VOWELS)
    else:
        word+=kind
print(word)