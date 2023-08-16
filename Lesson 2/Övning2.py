print("Välkommen till miniräknaren")

print("Du kan välja mellan dessa operatorer: ")
print("+")
print("-")
print("*")
print("/")

operator = input("Operator: ")

if operator in ("+", "-", "*", "/"):
    a = int(input("Tal 1: "))
    b = int(input("Tal 2: "))

    if operator == "+":
        print(a+b) 
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    else:
        if b == 0:
            print("Du kan inte dela med 0")
        else:
            print(a/b)
else:
    print("Du måste välja mellan operatorerna över")