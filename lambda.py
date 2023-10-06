import datetime
j=datetime.datetime.now()
print(j)
add=lambda x,y : x+y
print(add(2,4))
#different programe

a=[[1,3],[6,2],[9,4],[12,7]]
a.sort(key=lambda x:x[0])
print(a)
#different programme

import random
list=["bed","sheet","pen","pencil","laptop"]
select=random.choice(list)
print(select)
