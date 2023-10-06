# numbers=["23","45","67","678"]
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
# numbers=list(map(int,numbers))
# numbers[2]=numbers[2]+5
# print(numbers)
#
# num=[2,5,8,9,4,6,3,1]
# square=list(map(lambda x:x*x,num))
# print(square)
# print("\n")
# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# func=[square, cube]
# for i in range(5):
#     value=list(map(lambda x:x(i),func))
#     print(value)
# list1=[1,2,3,4,5,6,7,8,9,7,6,44,33,5,6]
# def function(number):
#     return number>6
# value=list(filter(function,list1))
# print(value)
from functools import reduce
list2=[1,2,3,4,5,6,7,8,9]
# num=0
# for i in list2:
#     num=num+i
# print(num)
num=reduce(lambda x,y:x+y,list2)
print(num)