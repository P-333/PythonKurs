"""
Äter upp vokalerna på ett ord.
"""
word = input("Vad är ditt ord? \n").upper()

VOWELS = ("A", "E", "I", "O", "U")

for letter in word:
    if letter not in VOWELS:
        print(letter)
