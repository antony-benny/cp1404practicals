# Question 1: Ask the user for their name and write it to name.txt
name = input("Please enter your name: ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# Question 2: Read the name from name.txt and print the greeting
file = open('name.txt', 'r')
name_from_file = file.readline().strip()  # Use readline() to get the name
file.close()
print(f"Hi {name_from_file}!")

# Question 3: Read the first two numbers from numbers.txt and print their sum
# Ensure to create numbers.txt with the specified numbers first
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline().strip())  # Read first line
    second_number = int(file.readline().strip())  # Read second line
    sum_of_two = first_number + second_number
    print(sum_of_two)  # Should print 59 if the numbers are correct

# Question 4: Print the total for all lines in numbers.txt
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:  # Using for line in file to read all lines
        total += int(line.strip())  # Accumulate the total
    print(total)  # This will print the total of all numbers
