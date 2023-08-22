hidden_number = 10

while True:
    guessedNumber = int(input("Vilket nummer gissar du på? \n"))

    if(guessedNumber == hidden_number):
        print("Du gissade rätt")
        break
    else:
        print("Ha ha! You're stuck in my loop!")