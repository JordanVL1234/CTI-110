###   JORDAN VICENTE-LACHAPELLE /-/ 10-10-2023 /-/ P2HW2   ###
import os
os.system('cls')

Grades = [
    float(input("Enter grade for Module 1: \n  ")),
    float(input("Enter grade for Module 2: \n  ")),
    float(input("Enter grade for Module 3: \n  ")),
    float(input("Enter grade for Module 4: \n  ")),
    float(input("Enter grade for Module 5: \n  ")),
    float(input("Enter grade for Module 6: \n  "))
]

###   CODE THAT WASEN'T ALLOWED 🙄   ###
# TAsked = 1
# while TAsked <= 6:
#     Grades.append(float(input(f"Enter grade for Module {TAsked}: \n  ")))
#     TAsked += 1

print("\n------------ Results ------------")
print(f"Lowest Grade: \n  {min(Grades)}")
print(f"Highest Grade: \n  {max(Grades)}")
print(f"Sum of Grade: \n  {sum(Grades)}")
print(f"Average: \n  {sum(Grades) / len(Grades)}")
print("-----------------------------------")