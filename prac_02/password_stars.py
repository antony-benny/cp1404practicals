"""Password input program with error-checking."""

MIN_PASSWORD_LENGTH = 8

def main():
    """Main function to run the password input program."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Function to prompt the user for a password and validate its length."""
    while True:
        password = input("Enter your password (at least {} characters): ".format(MIN_PASSWORD_LENGTH))
        if len(password) >= MIN_PASSWORD_LENGTH:
            return password
        print("Password is too short. Please try again.")

def print_asterisks(password):
    """Function to print asterisks corresponding to the password length."""
    print('*' * len(password))

if __name__ == "__main__":
    main()
