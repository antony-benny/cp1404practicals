CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

state_code = input("Enter short state: ")
while state_code:
    print(CODE_TO_NAME.get(state_code, "Invalid short state"))
    state_code = input("Enter short state: ")
