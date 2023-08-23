"""
Random number guesser
"""
# pylint: disable=import-self
from random import randrange


randomNumber = randrange(1, 10)
print(randomNumber)

while True:
    guessNumber = input("Guess a number between 1 - 10\n")
    numberParsed = int(guessNumber)
    if numberParsed == randomNumber:
        print("Rätt Nummer")
        break
    else:
        print("Fel nummer")
