def solve(a,b):
    c = a/b
    print(c)

try:
    solve(10)
except:
    print("there is an error")

# index error
I = [1,2,3,4,5,6]
try:
    print(I[8])
except IndexError:
    print("list out of range")
else:
    print("hello")
# finally execute every condition whatever error comes or not
finally:
    print("this is finally block")
