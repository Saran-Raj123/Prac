CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}
for state_acronym, state_abbreviation in CODE_TO_NAME.items():
    print("{:<3} is {:<3}".format(state_acronym, state_abbreviation))
state = input("Enter short state: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print("{:<3} is {:<3} \n".format(state, CODE_TO_NAME[state]))
    else:
        print("Invalid short state \n")
    for state_acronym, state_abbreviation in CODE_TO_NAME.items():
        print("{:<3} is {:<3}".format(state_acronym, state_abbreviation))
    state = input("Enter short state: ").upper()