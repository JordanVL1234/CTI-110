###   JORDAN VICENTE-LACHAPELLE /-/ 10/3/23 /-/ CALCULATE THE MONEY NEEDED TO DRIVE 3 DISTANCES   ###

miles = float(input("Miles/Gallon:\n    "))
dollars = float(input("Dollars/Gallon:\n    "))

Output20 = (20/miles)*dollars
Output75 = (75/miles)*dollars
Output500 = (500/miles)*dollars

print(f"Your Output:\n    20 Miles = ${Output20:.2f}\n    75 Miles = ${Output75:.2f}\n    500 Miles = ${Output500:.2f}")