line=" list topic "
print(line.capitalize().center(50,"*"),"\n")

print("list:- store maltiple values in single variable")
print("list:- list is mutable mean we can change the value of list")
numbers=[1,2,3,4,5]
print("numbers:-",numbers)
print(numbers[2])
print("type:-",type(numbers))

numbers[2]=10
numbers = numbers + [11,12,13]
print(numbers[-1])


print("numbers",numbers)
print(numbers[-1])

numbers.append(6)
print("numbers:-",numbers)
number=list(range(1,21))
print("number:-",number)

numbers.insert(2,50) 
print("numbers:-",numbers)
numbers.remove(6)
print("numbers:-",numbers)


num=list(map(int,input("enter the number:-").split()))
print("num:-",num)







