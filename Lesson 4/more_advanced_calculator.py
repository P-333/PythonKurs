"""
MORE ADVANCED CALCULATOR
"""

import math


while True:
    print("""----------------
Välkommen till miniräknaren

Du kan välja mellan dessa operatorer:
1 : +
2 : -
3 : *
4 : /
5 : √
6 : Avsluta
----------------

    """)

    operator = input("Operator: ")

    if operator == "6":
        print("Tack för du använde miniräknaren")
        break

    if operator in ("1", "2", "3", "4", "5"):
        a = int(input("Tal 1: "))
        if operator != "5":
            b = int(input("Tal 2: "))

        match operator:
            case("1"):
                print(f"{a} plus {b} = {a+b}")
            case("2"):
                print(f"{a} minus {b} = {a-b}")
            case("3"):
                print(f"{a} gånger {b} = {a*b}")
            case("4"):
                if b == 0:
                    print("Du kan inte dela med 0")
                else:
                    print(f"{a} dividerat med {b} = {a/b}")
            case("5"):
                print(f"Roten ur {a} = {math.sqrt(a)}")

    else:
        print("Du måste välja mellan operatorerna över")
