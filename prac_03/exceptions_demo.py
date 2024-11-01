"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A valueError occurs if the user enters something that isn't a valid number, like a letter or a decimal
2. When will a ZeroDivisionError occur?
A zeroDivisionError occurs if the user enters 0 as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, I could check if the denominator is zero before performing the division
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")