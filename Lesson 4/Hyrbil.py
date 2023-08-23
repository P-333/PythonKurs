try:
    resDistans = int(input("Hur många km ska du resa? "))
except ValueError:
    print("Du måste skriva in ett tal.")
    
hyrBilAKostnad = 1000
hyrBilBKostnad = resDistans * 2

if hyrBilBKostnad > hyrBilAKostnad:
    print(f"Hyrbil A är billigast, {hyrBilAKostnad} kr istället för {hyrBilBKostnad} kr")
else:
    print(f"Hyrbil B är billigast, {hyrBilBKostnad} kr istället för {hyrBilAKostnad} kr")