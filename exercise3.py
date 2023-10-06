n=18
i=4
while i>=0:
    n1=int(input("Please enter your number :\n"))
    if n1<n:
        print("Try higher, You have", i,"attempts left.\n")
    elif n1>n:
        print("Try lower, You have", i,"attempts left.\n")
    else:
        print("congrates!, You have guessed the correct number.\n")
        break
    i-=1
    if i==-1:
      print("YOU LOST")