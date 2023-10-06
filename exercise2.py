print("Enter your first no.")
num1=int(input())
print("Enter your second no.")
num2=int(input())
print("please enter your operator")
op=(input())
if op=='+':
    if num1==56 and num2==9:
        result=555
    else:
        result=num1+num2
elif op=='-':
    if num1==56 and num2==9:
        result=555
    else:
        result=num1-num2
elif op==('*'):
    if num1==56 and num2==9:
        reslt=555
    else:
        result=num1*num2
elif op=='/':
    if num1==56 and num2==9:
        result=555
    else:
        result=num1/num2
else:
    print("Wrong operator")
print("your desired output is:")
print(result)
