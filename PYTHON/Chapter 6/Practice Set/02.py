sub1 = int(input("Enter Bangla Subject marks : "))
sub2 = int(input("Enter English Subject marks : "))
sub3 = int(input("Enter Math Subject marks : "))

Total = sub1+sub2+sub3
Percentage = Total/3

if(Percentage>=40 and sub1>=30 and sub2>=33 and sub3>=33):
    print("This student passed")

else:
    print("This Student Fail")