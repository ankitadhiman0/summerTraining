class solution:
    def add(a,b):
        print(a+b)
    def sub(a,b):
        print(a-b)
    def mul(a,b):
        print(a*b)
    def div(a,b):
        print(a/b)
print("press 1 for addition")
print("press 2 for substraction")
print("press 3 for multiplication")
print("press 4 for division")
u = int(input("enter your option"))
a = int(input("enter ist value"))
b = int(input("enter second value"))
if u==1:
    solution.add(a,b)
elif u==2:
    solution.sub(a,b)
elif u==3:
    solution.mul(a,b)
elif u==4:
    solution.div(a,b)
else:
    print("invalid input")

    