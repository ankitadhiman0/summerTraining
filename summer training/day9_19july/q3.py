# write aa program to print the fibonacci series upto a given number using while loop
number = int(input("enter a number"))
first_number = 0
second_number = 1
a = 0
if number<=0:
    print("enter a positive number")
elif number == 0:
    print("fibonacci series upto ",number,":",first_number)
else:
    print("fibonacci series upto:",number,"terms")
    while a<number:
        print(first_number)
        next = first_number + second_number
        first_number = second_number
        second_number = next
        a+=1