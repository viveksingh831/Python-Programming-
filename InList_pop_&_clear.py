num=[1,2,3,4,5,6,7,8,9,10]
print("numbers:-",num)
print("pop method:- pop method is used to remove the last element of list and return it")
x=num.pop()
print("x(popped):-",x)
print("numbers:-",num)
x=num.pop(2)
print("x(popped):-",x)
print("Numbers:-",num,"\n")
print("clear method:- clear method is used to remove all the elements of list")
num.clear()
print("numbers:-",num,"\n")
print("index method:- index method is used to find the index of an element in list")
num1=[1,2,3,4,5,9,7,8,6]
print("numbers:-",num1)
print("index of 5:-",num1.index(5),"\n")
print("sort method:- sort method is used to sort the elements of list in ascending order")
num1.sort()
print("numbers:-",num1)
num2=[3,6,2,7,4,9,12,16]
print("numbers:-",num2,"\n")
print("reverse method:- reverse method is used to reverse the elements of list")
num2.reverse()
print("numbers:-",num2,"\n")
print("sort(reverse=True):- sort(reverse=True) method is used to sort the elements of list in descending order")
num2.sort(reverse=True)
print("numbers:-",num2,"\n")

print("copy method:- copy method is used to copy the elements of list into another list")
num3=num2.copy()
num3.append(21)
print("numbers:-",num3,"\n")

print("len method:- len method is used to find the length of list")
print("length of num3:-",len(num3),"\n")

print("min method:- min method is used to find the minimum element of list")
print("minimum element of num3:-",min(num3),"\n")

print("max method:- max method is used to find the maximum element of list")
print("maximum element of num3:-",max(num3),"\n")

print("sum method:- sum method is uded to find the sum of all the elements of list")
print("sum of all the elements of num3:-",sum(num3),"\n")

print("in operator:- in operator is used to check whether an element is present in list or not")
print("is 21 present in num3:-",21 in num3,"\n")

print("not in operator:- not in operator is used to check whether an element is not present in list or not")
print("is 22 not present in num3:-",22 not in num3,"\n")

print("list comprehension:- list comprehension is used to create a new list from an existing list")
num4=[x for x in num3 if x%2==0]
print("even numbers in num3:-",num4)
squares=[x**2 for x in num3]
print("squares of elements in num3:-",squares)

