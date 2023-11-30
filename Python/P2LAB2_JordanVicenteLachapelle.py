import os
os.system('cls')

Num1 = float(input("Input your first number: \n  "))
Num2 = float(input("Input your second number: \n  "))
Num3 = float(input("Input your third number: \n  "))
Num4 = float(input("Input your fourth number: \n  "))

Product = f"{(Num1 * Num2 * Num3 * Num4):.3f}"
ProductR = f"{float(Product):.1f}"
Avg = (Num1 + Num2 + Num3 + Num4) / 4
AvgF = f"{Avg:.3f}"

print(f"\nOutput - \n  The product rounded (1 decimal): {ProductR}\n  The product is: {Product}\n  The average as a floating-point: {AvgF}")