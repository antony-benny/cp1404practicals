"""
emails.py
Estimate: 10 minutes
"""


def extract_name(email):
    """Extracts a name from the email."""
    return email.split('@')[0].replace('.', ' ').title()

email_dict = {}

while True:
    email = input("Email: ")
    if email == "":
        break

    name = extract_name(email)
    confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()

    if confirm not in ('y', 'yes', ''):
        name = input("Name: ")

    email_dict[email] = name

for email, name in email_dict.items():
    print(f"{name} ({email})")
