"""
Tar in en poängsats och tittar om man är godkänd eller inte
"""
try:
    betyg = int(input("Hur många poäng fick du? "))
except ValueError:
    print("Du måste skriva in ett tal.")
if betyg >= 20:
    print("Du fick godkänt!")
else:
    print("Du fick inte godkänt :(")
