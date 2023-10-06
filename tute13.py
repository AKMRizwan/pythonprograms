var1=18
var3="yes"
print("Please enter your age:")
age=int(input())
if age<7:
    print("please enter correct age")
elif age>90:
    print("you are over aged")
else:
    print("your age is correct, lets check your eligibility")
print("do you want to proceed")
ans=input()

if ans==var3:

    if age<var1:
        print("Not eligible")
    elif age==var1:
        print("Can't decide must attend pyhsically")
    else:
        print("congrates! You are eligible")

else:
     print("thank you for using our services")
