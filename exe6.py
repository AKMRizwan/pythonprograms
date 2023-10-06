import random
You =0
Computer=0
for i in range (10):
    User=input("Please enter your choice\n")
    list=["Snake","Water","Gun"]
    System=random.choice(list)
    print("Your opponent choice is: ",System)
    print(User,"V/S",System)
    if User=="snake" and System=="Water":
        print("Congrates! You won")
        You+=1
    elif User=="snake" and System=="Gun":
        print("You lost")
        Computer+=1
    elif User=="water" and System=="Snake":
        print("You lost")
        Computer+=1
    elif User=="water" and System=="Gun":
        print("Congrates! You won")
        You+=1
    elif User=="gun" and System=="Water":
        print("You lost")
        Computer+=1
    elif User=="gun" and System=="Snake":
        print("Congrates! You won")
        You+=1
    elif User=="snake" and System=="Snake":
        print("Game tie")
    elif User=="water" and System=="Water":
        print("Game tie")
    elif User=="gun" and System=="Gun":
        print("Game tie")
    else:
        print("Wrong choice")
print("\n")
print("Final Score")
print(You ,"V/S", Computer)
if You>Computer:
    print("You won")
elif You < Computer:
    print("You Lost")
else:
    print("Game tie")