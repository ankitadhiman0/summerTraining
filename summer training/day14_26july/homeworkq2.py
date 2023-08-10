def prime(n):
  list =[]
  list2 =[]
  for x in range(2,n+1):
    if x > 1:
        for i in range(2, x): 
             if x % i == 0:
                break
        else:
             list.append(x)
  for x in range(0,len(list)-1):
     if list[x]%2==0:
       list2.append(list[x])
       print("even prime number",list[x])
a = int(input("enter a  number"))
prime(a)