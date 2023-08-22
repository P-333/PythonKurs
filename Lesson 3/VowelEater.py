word = input("Vad är ditt ord? \n").upper()

word = tuple(word)

vowels = ("A", "E", "I", "O", "U")

for letter in word:
    if letter not in vowels:
        print(letter)