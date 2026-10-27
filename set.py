line=" set chapeter in python "
print("\n",line.center(50,"*"))
num={1,2,3,4,5,6,7,8,9,9}
print("numbers:-",num)
print("set store unique value its not store duplicate value")
print(len(num))
print("tpye:-",type(num),"\n")

print("add method:- add method store new value in set")
num.add(10)
print("numbers;-",num,"\n")

print("update method:- update method store new multiple value in set")
num.update([11,12,13,14])
print("numbers:-",num,"\n")

print("remove method:- remove method remove element from set if not found then error")
num.remove(14)
print("remove:-",num)
#num.remove(14)
print("remove:-",num,"\n")

print("discard method:- discard method discard element from the set if not foun then its not give error")
num.discard(13)
print("numbers:- 13",num)
num.discard(13)
print("discard:- 13",num,"\n")

print("pop method:- pop method remove any element from the set")
num.pop()
print("numbers:-",num,"\n")

print("clear method:- clear method remove all element from the set")
num.clear()
print("numbers:-",num)
print(len(num),"\n")

print("union(|) method:- union method give all unique element from the both sets")
a={1,2,3,4}
b={4,5,6,7}
print("union (a|b):-",a|b,"\n")

print("intersection(&) method:- intersection method give common element in both sets")
print("intersection(&):-",a&b,"\n")

print("difference (-) method:- difference method give these element that 1st set element not presen 2nd set")
print("difference:-",a-b)
print("difference:-",b-a,"\n")

print("symmetric(^) method:- symmetric method give these element that not common in the both sets")
print("symmetric:-",a^b,"\n")

print("In method:- In method give True & false if element presen in set then True otherwise false")
num1={1,2,3,4,5,6}
print("numbers:-",num1)
print("In(5):-",5 in num1)
print("In (7):-",7 in num1,"\n")

print("Not in method:- Not in method give True & false if element not present in the set the True otherwise false")
print("Not in (7):-", 7 not in num1)
print("Not in (5):-",5 not in num1)





