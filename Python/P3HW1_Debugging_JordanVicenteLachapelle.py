###   JORDAN VICENTE-LACHAPELLE /-/ 10/19/23 /-/ DEBUGGED CODE   ###

import os
os.system('cls')

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
print("------------ Results ------------")
low = min(grades)
print(f"Lowest Grade:            {low}")
high = max(grades)
print(f"Highest Grade:           {high}")
sum = sum(grades)
print(f"Sum of Grades:           {sum}")
avg = sum/len(grades)
print(f"Average:                 {avg}")

# determine letter grade for average

print("---------------------------------")
if avg >= 90:
    print('Your grade is: A\n')
elif avg >= 80:
    print('Your grade is: B\n')
elif avg >= 70:
    print('Your grade is: C\n')
elif avg >= 60:
    print('Your grade is: D\n')
else:
    print('Your grade is: F\n') # TO DO: finish this