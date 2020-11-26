"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score > 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
