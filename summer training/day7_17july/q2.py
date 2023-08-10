angle1 = int(input("enter angle1"))
angle2 = int(input("enter angle2"))
angle3 = int(input("enter angle3"))
if angle1<90 and angle2<90 and angle3<90:
    print("acute angled triangle")
elif angle1==90 or angle2==90 or angle3==90 and sum<=180:
    print("right angled triangle")
elif angle1>90 or angle2>90 or angle3>90 and sum<=180:
    print("obtuse angled triangle")
else:
    print("triangle is not exit")