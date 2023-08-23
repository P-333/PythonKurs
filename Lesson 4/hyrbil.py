"""
Tar in ett kilometer tal och tittar om Hyrbil A eller Hyrbil B är billigast
"""
try:
    resDistans = float(input("Hur många km ska du resa? "))
except ValueError:
    print("Du måste skriva in ett tal.")

HYB_BIL_A_KOSTNAD = 1000
HYR_BIL_B_KOSTNAD = resDistans * 2

if HYR_BIL_B_KOSTNAD > HYB_BIL_A_KOSTNAD:
    print(f"Hyrbil A är billigast, {HYB_BIL_A_KOSTNAD} kr istället för {HYR_BIL_B_KOSTNAD} kr")
else:
    print(f"Hyrbil B är billigast, {HYR_BIL_B_KOSTNAD} kr istället för {HYB_BIL_A_KOSTNAD} kr")
