"""
CP1404 - Practical
Pseudocode for sales_bonus

sales = 0
while sales >= 0
key in sales
if sales >= 100
bonus = sales * 0.15
display bonus
elif sales>= 0
bonus = sales * 0.10
display bonus
else
display negative sales
"""

"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = 0
while sales >= 0:
    sales = float(input("Enter sales: $"))
    if sales >= 1000:
        print("your bonus is: ", sales * 0.15)
    elif sales >= 0:
        print("your bonus is: ", sales * 0.10)
    else:
        print("Negative sales")
