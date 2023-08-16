print("Välkommen till quizen")
name = str(input("Vad är ditt användarnamn"))

points = 0

frågor = ("Fråga 1", "Fråga 2", "Fråga 3")
svar = ("svar", "svar", "svar")

for idq, q in enumerate(frågor):
    fråga = str(input(q))

    if (fråga == svar[idq].lower()):
        print("Rätt svar " + name)
        points += 1
    else:
        print("Fel svar")