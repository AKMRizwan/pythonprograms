def function(*args, **kwargs):

    for item in ar:
        print(item)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
ar = ["bed","sheet","pen","keyboard"]
kwrg = {"laptop":"hardware","antivirus":"software","hand":"part","man":"homosapien"}
function(*ar, **kwrg)