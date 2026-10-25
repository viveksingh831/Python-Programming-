line="Tuples in python"
print(line.center(50,'*'))
num=(1,2,3,4,5,6,7,8,9,2,4,6,7)
print("number:-",num)
print("index of 5:-",num[5])
print("index of -1:-",num[-1])
print("type:-",type(num),"\n")

print("tuple is immutable mean we can not change the value of tuple\n")
print("count method:- find total occurrences of element intuple")
print("count of 6:-",num.count(6),"\n")

print("index method:- index method find 1st element index in tuple")
print("index:-",num.index(5),"\n")

print("tuple packing:- store multiple value in one variable in form of tuple")
student="vivek",24,"CSE"
print("tuple packing:-",student,"\n")

print("Tuple unpacking:- assign value in defferent variable")
name,age,branch=student
print("unpacking:-",name)
print("unpacking:-",age)
print("unpacking:-",branch,"\n")

print("Tuple slicing:- ")
print("slicing:-",num[1:5])
print("slicing:-",num[:4])
print("slicing:-",num[::-1])

