def fun(number):
  for x in range(2, number):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            print(x)
a = int(input("enter a  number"))
fun(a)