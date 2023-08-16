import time

print("Initializing Temperature sensor... Please wait!")
time.sleep(5)
temp = int(input("Hur varmt är det?"))
while(True):
    if (temp < 10):
        print("Startar elementet")
        break
    else:
        print("Väntar 30 minuter")
        time.sleep(30*60)