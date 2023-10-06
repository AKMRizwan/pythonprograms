star=bool(int(input("Enter 1 for true and 0 for false\n")))
if(star==1):
    for i in range(5):
        print("*",i*" * ")
else:
    for i in range(4,-1,-1):
        print("*",i*" * ")