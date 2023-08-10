sub_1 = int(input("enter  marks"))
sub_2 = int(input("enter marks"))
sub_3 = int(input("enter marks"))
sub_4 = int(input("enter marks"))
sub_5 = int(input("enter marks"))
total_marks = (sub_1+sub_2+sub_3+sub_4+sub_5)
percentage = (total_marks/500)*100
if percentage>= 50:
    if percentage>=50 and percentage<=90:
        print("B garde")
    else:
        print("A grade")
else:
    print("fail")        