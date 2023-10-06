n = int(input("Enter the value of n: "))
is_true = bool(int(input("Enter 1 for True or 0 for False: ")))

if is_true:
    for i in range(1, n + 1):
        print("*" * i)
else:
    for i in range(n, 0, -1):
        print("*" * i)
