r=open("file.txt","rt")
print(r.readline())
print(r.readlines())

context=r.read()
print(context)
for line in r:
    print(line)
r.close()