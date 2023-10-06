n=18
i=4
while i>=0:
    n1=int(input("Enter your number:\n"))
    if n1<n:
        print("Wrong answer, Try Higher, Now you have",i," attempts left.\n")
    elif n1>n:
        print("Wrong answer, Try Lower, Now you have",i,"attempts left.\n")
    else:
        print("congrates! you have guessed the correct number.\n")
        break
    i-=1
    if i==-1:
        print("You have LOST the game, Better luck next time.\n")