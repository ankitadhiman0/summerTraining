sub1 = int(input("enter marks of sub1"))
sub2 = int(input("enter marks of sub2"))
sub3 = int(input("enter marks of sub3"))
sub4 = int(input("enter marks of sub4"))
sub5 = int(input("enter marks of sub5"))
percentage = (sub1+sub2+sub3+sub4+sub5)/500*100
if percentage>=60:
    print("pass")
if percentage<60:
    print("fail")

