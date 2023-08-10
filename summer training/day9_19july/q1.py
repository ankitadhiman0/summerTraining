# write a program to check if a given no. is prime no. using while loop
number = int(input("enter a number"))
a = 0
b = 2
while b<= number / 2:
    if number%b==0:
        a = 1
        break
    b = b+1
if a==0:
    print("prime number")
else:
    print("not prime number")    