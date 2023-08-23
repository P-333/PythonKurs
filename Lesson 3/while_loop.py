"""
A program that reads a sequence of numbers
and counts how many numbers are even and how many are odd.
The program terminates when zero is entered.
"""
ODD_NUMBERS = 0
EVEN_NUMBERS = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter
        ODD_NUMBERS += 1
    else:
        # Increase the even_numbers counter
        EVEN_NUMBERS += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", ODD_NUMBERS)
print("Even numbers count:", EVEN_NUMBERS)
