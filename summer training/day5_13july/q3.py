# percentage is less than 75% student will not able to sit in exam or will not able to sit in the exam
total_days = int(input("total number of working days"))
total_absent = int(input("number of days absent"))
present = total_days-total_absent
percentage = (present/total_days)*100
if percentage>=75:
    print("you are able to sit in the exam")
else:
    print("you are not able to sit in the exam")