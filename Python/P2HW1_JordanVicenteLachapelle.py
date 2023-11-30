import os
os.system('cls')

FName = input("First Name: \n  ")
HairC = input("Hair Color: \n  ")
EyeC = input("Eye Color: \n  ")
Height = float(input("Height in feet (Use a decimal point): \n  "))
Age = int(input("Age: \n  "))
FavFood = input("Favorite Food: \n  ")

Dict = {"First Name" : FName, "Hair Color" : HairC, "Eye Color" : EyeC, "Height" : Height, "Age" : Age, "Favorite Food" : FavFood}

print(f"\n{Dict['First Name']} is a {Dict['Height']} tall student with {Dict['Hair Color']} hair and {Dict['Eye Color']} eyes. They are {Dict['Age']} years old and their favotiye foor is {Dict['Favorite Food']}.")