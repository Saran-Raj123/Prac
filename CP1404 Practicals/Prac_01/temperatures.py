"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

Display menu
choice from menu
while choice not equal to choice in menu
Display invalid
if choice = c
key in the number
fahrenheit = celsius * 9.0 / 5 + 32
print the number into fahrenheit
else if the choice = f
key in the number
celsius = 5 / 9 * (fahrenheit - 32)
print the number into celsius
else print invalid
choice = q
print thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Enter Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")


