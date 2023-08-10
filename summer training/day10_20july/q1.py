#  even or odd
even = 0
odd = 0
for x in range(1,101):
    if (x%2==0):
       even=even+1
    else:
       odd=odd+1
print("even number",even)  
print("odd number",odd)