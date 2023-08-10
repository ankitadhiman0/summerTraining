def solve(a,b):
    c = a/b
    print(c)

try:
    solve(10,0)
except ZeroDivisionError:
    print("invalid input please check your number")
except TypeError:
    print("please provide complete values")