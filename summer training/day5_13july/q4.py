salary = int(input("enter your salary"))
bonous = (5/100)*salary
year_of_services = int(input("enter your year of working"))
print("your bonous = ",bonous)
net_salary = salary+bonous
if year_of_services>5:
    print("your net_salary = ",net_salary)
else:
    print("your net_salary is same ",salary)