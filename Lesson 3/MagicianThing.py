hidden_number = 10

while True:
    try:
        guessedNumber = int(input("Vilket nummer gissar du på? \n"))  
    except ValueError:
        print("Du måste ange ett nummer")
        continue
    except KeyboardInterrupt:
        print("Bra försök men mig lurar du inte!")
        continue
    except: 
        print("Något annat gick åt helvete, men du är fortfarande fast.")
        continue

    if guessedNumber == hidden_number:
        print("Du gissade rätt")
        break
    else:
        print("Ha ha! You're stuck in my loop!")