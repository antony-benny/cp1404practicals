"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def determine_score_status(score):
    """Return the score status based on the provided score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """Main function to get user input and print score status."""
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(determine_score_status(random_score))

if __name__ == "__main__":
    main()
