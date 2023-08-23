"""
MORE ADVANCED CALCULATOR
"""

import math

print("Välkommen till miniräknaren")

print("Du kan välja mellan dessa operatorer: ")
print("1 : +")
print("2 : -")
print("3 : *")
print("4 : /")
print("5 : √")

operator = input("Operator: ")

if operator in ("1", "2", "3", "4", "5"):
    a = int(input("Tal 1: "))
    if operator != "5":
        b = int(input("Tal 2: "))

    match operator:
        case("1"):
            print(a+b)
        case("2"):
            print(a-b)
        case("3"):
            print(a*b)
        case("4"):
            if b == 0:
                print("Du kan inte dela med 0")
            else:
                print(a/b)
        case("5"):
            print(math.sqrt(a))
else:
    print("Du måste välja mellan operatorerna över")
