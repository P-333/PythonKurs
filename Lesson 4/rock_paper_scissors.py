"""
A rock paper scissors game
"""
from random import randint

print("""
-----------
Välkommen till sten sax påse.
      
De olika valen du kan göra är:
    1. Sten
    2. Sax
    3. Påse

Lycka till!
-----------
""")

computer = randint(1,3)
player = int(input("Välj ditt drag: "))

if player not in (1, 2, 3):
    print("Du måste välja mellan 1, 2 eller 3")

# Win lose ratio
rps = ((-1, 1, 3), (1, -1, 2), (3, 2, -1))

result = rps[player-1][computer-1]

if player == result:
    print("Du vann")
elif computer == result:
    print("Datorn vann")
else:
    print("Det blev oavgjort")
