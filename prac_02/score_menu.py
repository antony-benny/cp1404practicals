"""
CP1404/CP5632 - Practical
Program to manage score status and display.
"""

def get_valid_score():
    """Get a valid score from the user (0-100 inclusive)."""
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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

def show_stars(score):
    """Print stars corresponding to the score."""
    print('*' * int(score))

def main():
    """Main function to run the menu program."""
    score = get_valid_score()

    while True:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_score_status(score)
            print(f"Score result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
