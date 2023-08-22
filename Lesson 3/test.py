while True:
    try:
        inp = float(input("Skriv in ditt nummer \n"))
    except:
        print("Något gick fel \n")
        continue
    
    cel = (inp - 32.0) * 5.0 // 9.0
    print(cel)