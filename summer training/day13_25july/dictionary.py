dic = {"name":"ram","age":25}
print(dic)
x = dic.keys() # fetch keys
print(x)
x = dic.items()
print(x)
x = dic.values()
print(x)
     
# searching
if "name" in dic:
    print("yes")
else:
    print("no")

# add data
dic["mobileno"] = 9015328568
dic.update({"mobileno":9015328568})
dic.pop("age")
print(dic)
for x in dic:
    print(x)
    for x in dic.items():
        print(x)

for x in dic.items():
    if 
