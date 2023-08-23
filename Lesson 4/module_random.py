"""
Ett program som tvingar dig att gissa ett nummer.
"""
from random import randint
HIDDEN_NUMBER = randint(1, 100000)

while True:
    try:
        guessedNumber = int(input("Vilket nummer gissar du på? \n"))
    except ValueError:
        print("Du måste ange ett nummer")
        continue
    except KeyboardInterrupt:
        print("Bra försök men mig lurar du inte!")
        continue

    if guessedNumber == HIDDEN_NUMBER:
        print("Du gissade rätt")
        break
    else:
        print("Ha ha! You're stuck in my loop!")
