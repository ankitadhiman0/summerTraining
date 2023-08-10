number = int(input("enter a number"))
last_digit = number/10
print("last_digit = ",last_digit)
if last_digit%3==0:
    print("number is divisible by 3")
if last_digit%3 !=0:
    print("number is not divisible by 3")
