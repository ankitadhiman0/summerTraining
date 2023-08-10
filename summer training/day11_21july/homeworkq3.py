a = int(input("enter a number"))
for row in range(1,a+1):
    for col in range(row,a):
        print(" ",end="")
    for col in range(0,2*row-1):
        print("*", end= "")
    print()
     