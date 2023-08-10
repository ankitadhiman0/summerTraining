# given number is palindrome using while loop
num = int(input("enter a number"))
denum = num
rem = 0
rev = 0 
# print("num")
while(num!=0):
        rem = num%10
        rev = rev*10+rem
        num = num//10
print(num) == 0
if(rev == denum):
        print("it is a palidrome")
else:
        print("it is not a palidrome")

