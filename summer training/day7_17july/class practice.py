sub_1 = int(input("enter  marks"))
sub_2 = int(input("enter marks"))
sub_3 = int(input("enter marks"))
sub_4 = int(input("enter marks"))
sub_5 = int(input("enter marks"))
total_marks = (sub_1+sub_2+sub_3+sub_4+sub_5)
percentage = (total_marks/500)*100
if percentage>45 and percentage<=60:
    print("D grade")     
elif percentage>60 and percentage<=75:
    print("C grade")
elif percentage>75 and percentage<=85:
    print("B grade")
elif percentage>85 and percentage<=100:
    print("A grade")   
elif percentage<45:
    print("fail")
else:
    print("error")