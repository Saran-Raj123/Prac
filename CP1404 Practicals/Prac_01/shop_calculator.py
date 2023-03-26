"""
CP1404 - Practical
Pseudocode for broken_score

input number of items
while items <= 0
display 1 or more item is required
input items
item = 1
total = 0
while item <= items
input price
item = item + 1
total = price + total
if total > 100
total = total - (total * 0.9)
display number of items and price
else
display number of items and price
"""

items = int(input("Number of items? "))
while items <= 0:
    print("1 or more item is required.")
    items = int(input("Number of items? "))
item = 1
total = 0
while item <= items:
    price = float(input("Price of item: "))
    item = item + 1
    total = price + total
if total > 100:
    total = total - (total * 0.9)
    print(f"For {items} items the total price is ${total:.2f}")
else:
    print(f"For {items} items the total price is ${total:.2f}")
