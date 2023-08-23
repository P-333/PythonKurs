"""
Quiz uppgift
"""
print("Välkommen till quizen")
NAME = str(input("Vad är ditt användarnamn"))

POINTS = 0

QUESTIONS = ("Fråga 1", "Fråga 2", "Fråga 3")
ANSWERS = ("svar", "svar", "svar")

for idq, q in enumerate(QUESTIONS):
    QUESTION = input(q)

    if QUESTION == ANSWERS[idq].lower():
        print("Rätt svar " + NAME)
        POINTS += 1
    else:
        print("Fel svar")
        