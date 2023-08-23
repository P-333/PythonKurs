"""
Simple time calculator
"""
import sys

print("Välkommen till att räkna ut tiden")

startTidTimme = int(input("Vilken starttimme(00 till 23): "))

if startTidTimme > 23 or startTidTimme < 0:
    print("Måste välja ett tal mellan 00 och 23")
    sys.exit("Fel tid angiven")

startTidMinut = int(input("Vilken startminut: "))

if startTidMinut > 59 or startTidMinut < 0:
    print("Måste välja ett tal mellan 0 och 59")
    sys.exit("Fel tid angiven")

antalMinuterTillSlut = int(input("Antal minuter: "))

if antalMinuterTillSlut < 1:
    print("Du måste skriva ett tal större än 1")
    sys.exit("Fel tid angiven")



endHour = (startTidTimme + ((antalMinuterTillSlut + startTidMinut) // 60)) % 24
endMinut = (startTidMinut + antalMinuterTillSlut) % 60

print(str(endHour) + ":" + str(endMinut))
