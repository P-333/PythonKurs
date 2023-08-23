"""
User will input a word then input a string with random characters
The program will see if the random string contains the chars from the word in the right order.
"""
word = input("Input a word: ")
randomChars = input("Spamm random characters: ")

LATEST_POS = 0
FOUND = True

for letter in word:
    LATEST_POS = randomChars.find(letter, LATEST_POS)
    if LATEST_POS == -1:
        FOUND = False
        break

RESULT = "Yes, the random characters contain the chars from the word in the right order" \
    if FOUND else "Den hittades inte"

print(RESULT)
