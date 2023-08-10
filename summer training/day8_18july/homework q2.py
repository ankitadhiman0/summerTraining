# sum of the digits of a given number using while loop
print("enter a number")
number = int(input())
sum = 0
while number>0:
        rem = number%10
        sum = sum+rem
        number = int(number/10)
print("sum of digits of given number:",sum)