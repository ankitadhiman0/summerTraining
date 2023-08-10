a = [1,5,8,9,0,4,3,6,7,13,24,56,46,78,90,22,33,1156,78,98,90]
odd = []
even =[]
count_odd=0
count_even=0
for x in range(0,len(a)):
    if(a[x]%2==0):
        count_even+=1
        even.append(a[x])
    else:
        count_odd+=1
        odd.append(a[x])

print("odd list=", odd)
print("even list=",even)
# count even odd numbers

print("odd list = ",count_odd)
print("even list = ",count_even)