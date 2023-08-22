while True:
    year = int(input("Vilket år vill du titta skottår eller inte?"))

    if year < 1582:
        print("Not within the Gregorian Calendar period")
    else:
        if year % 4 != 0:
            print("Vanligt år")
        elif year % 100 != 0:
            print("Skottår")
        elif year % 400 != 0:
            print("Vanligt år")
        else: 
            print("Skottår")