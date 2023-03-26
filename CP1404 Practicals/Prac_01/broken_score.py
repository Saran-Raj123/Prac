"""
CP1404 - Practical
Pseudocode for broken_score

input score
if score > 100 or < 0
display invalid
else if score >= 90
display excellent
else if score >= 50
display passable
else
display bad

"""

score = float(input("Enter score: "))

if score > 100 or score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
