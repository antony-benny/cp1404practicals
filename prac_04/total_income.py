"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))  # Kept variable name

    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Changed to f-string
        incomes.append(income)

    print_income_report(incomes, months)  # Call the new function


def print_income_report(incomes, months):
    """This function will print the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
