import random

randomNumber = random.randrange(1, 10)
print(randomNumber)

while(True):
    guessNumber = input("Guess a number between 1 - 10\n")
    numberParsed = int(guessNumber)

    if(numberParsed == randomNumber): 
        print("Rätt Nummer")
        break
    else:
        print("Fel nummer")

