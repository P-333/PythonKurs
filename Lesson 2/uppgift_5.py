"""
Simple multi math problem
"""
INPUT = (0, 1, -1)

for x in INPUT:
    x = float(x)
    y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
    print("y=", y)
