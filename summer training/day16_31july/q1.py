class solution:
 def add(a,b):
    print(a+b)
 def sub(a,b):
    print(a-b)
 def divide(a,b):
    print(a/b)
 def mul(a,b):
    print(a*b)

print("enter 1 for addition")
print("enter 2 for multiply")
print("enter 3 for subtraction")
print("enter 4 for division")
q = int(input("enter your option"))
a = int(input("enter 1st value"))
b = int(input("enter 2nd value"))
if q==1:
   solution.add(a,b)
elif q==2:
   solution.mul(a,b)
elif q==3:
   solution.sub(a,b)
elif q==4:
    solution.divide(a,b)
else:
   print("invalid input")