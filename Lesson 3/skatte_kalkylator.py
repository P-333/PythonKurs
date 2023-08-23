"""
Skattekalkylator som tar in en årslön och kalkylerar skatten beroende på hur mycket du tjänar
"""
income = float(input("Hur mycket Thalers tjänade du: \n"))

if income < 85528:
    tax = income * 0.18 - 556
    print(round(tax))
else:
    incomeAfterPrelTax = income - 14839
    if incomeAfterPrelTax > 85528:
        incomeOverLimit = incomeAfterPrelTax - 85528
        tax = (incomeOverLimit * 0.32) + 14839
        print(round(tax))
    else:
        print(round(14839))
