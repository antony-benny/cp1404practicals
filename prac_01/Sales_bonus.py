"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Get sales
sales = float(input("Enter sales: $"))

# Loop until sales is negative
while sales >= 0:
    # Calculate bonus
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus
    else:
        bonus = sales * 0.15  # 15% bonus

    # Print bonus
    print(f"Bonus: ${bonus:.2f}")

    # Get sales again
    sales = float(input("Enter sales: $"))

print("Thank you.")
