"""
Implementation av Collatz teorin
"""
c0 = int(input("Ge mig ett nummer som inte är negativt eller 0: "))

STEPS = 0

if c0 <= 0:
    print("Ditt nummer måste vara positivt och inte noll")

while c0 != 1:
    STEPS += 1
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = (c0 * 3) + 1

print("Du klarade det i " + str(STEPS) + " steg")
