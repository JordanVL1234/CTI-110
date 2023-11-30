import os
os.system('cls')

YearIn = int(input("Enter what year it is : \n"))

if YearIn % 4 == 0:
    if YearIn / 100 == 0:
        if YearIn % 400 == 0:
            IsLeap = True
        else:
            IsLeap = False
    else:
        IsLeap = True
else:
    IsLeap = False
    
if IsLeap == True:
    print(f"{YearIn} is a leap year.!")
else:
    print(f"{YearIn} is not a leap year.")