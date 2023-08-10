# calculate income tax
tax_rate = 6
standard_deduction = 3000
each_dependent = 400
gross_income = int(input("enter your gross income"))
net_income = gross_income-standard_deduction-each_dependent
income_tax = (net_income/gross_income)*100
print("income_tax =",income_tax)