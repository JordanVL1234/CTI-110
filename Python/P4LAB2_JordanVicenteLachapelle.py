in1 = int(input("Put your first number : \n  "))
in2 = int(input("Put your second number : \n  "))
TrueRun = 0

while TrueRun != 1:
    if in2 >= in1:
        print(in1)
        in1 = in1 + 5
    if in1 == in2:
        print(in1)
        in1 = in1 + 5
        TrueRun = 1
    elif in2 < (in1 - 5):
        print("Second integer can't be less than the first.")