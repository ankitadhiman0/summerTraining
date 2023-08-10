r = int(input("enter the number of rows in a triangle"))
for a in range(1,r+1):
    for b in range(r,a,-1):
        print(" ",end = " ")
    for c in range(1,a+1):
        print("*",end = " ")
    for d in range(2,a+1):
        print("*",end =" ")
    print()