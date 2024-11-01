"""
CP1404/CP5632 - Practical
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # this line
    except ValueError:  # add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
