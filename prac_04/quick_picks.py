import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    # Ask the user how many quick picks to generate
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        # Generate a quick pick
        quick_pick = generate_quick_pick()
        # Print the quick pick in sorted order
        print(" ".join(f"{num:2}" for num in sorted(quick_pick)))


def generate_quick_pick():
    """Generate a list of 6 unique random numbers."""
    pick = set()
    while len(pick) < NUMBERS_PER_PICK:
        pick.add(random.randint(MIN_NUMBER, MAX_NUMBER))
    return list(pick)


# Run the program
main()
