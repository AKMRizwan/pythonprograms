print("Please enter your choice\n"
      "1 for Harry\n"
      "2 for Rohan\n"
      "3 for Hammad\n")
p=int(input())
if p==1:
      print("What do you want to open Harry's diet file or exercise file\n"
      "1 for Diet\n"
      "2 for exercise\n")
      deh=int(input())
      if deh==1:
            with open("harrydiet.txt") as f :
                  print(f.read())
      elif deh==2:
            with open("harryexercise.txt") as f :
                  print(f.read())
      else:
            print("Wrong choice")
elif p==2:
      print("What do you want to open Rohan's diet file or exercise file\n"
            "1 for Diet\n"
            "2 for exercise\n")
      der=int(input())
      if der==1:
          with open("rohandiet.txt") as f:
              print(f.read())
      elif der==2:
          with open("rohanexercise.txt") as f:
              print(f.read())
      else:
          print("Wrong choice")
elif p==3:
    print("What do you want to open Hammad's diet file or exercise file\n"
          "1 for Diet\n"
          "2 for exercise\n")
    dem=int(input())
    if dem==1:
        with open("hammaddiet.txt") as f:
            print(f.read())
    elif dem==2:
        with open("harryexercise.txt") as f:
            print(f.read())
    else:
        print("Wrong choice")