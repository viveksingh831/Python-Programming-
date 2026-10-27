line=" \nDictionary Chapter in the python "
print(line.center(50,'*'))
print("Dictionary use to store value like key and these value in the python")
student={"name":"Vivek kumar singh","age":"24","branch":"CSE","Cource":"B.tech"}
print(student)
print(student["name"])
print(len(student),type(student),"\n")


print("Update value in the dictionary:-")
student["age"]=22
print(student)
print("new value of age:- ",student["age"],"\n")

print(" Add new key:value in the dictionary:-")
student["city"]="Bhopal"
print(student)
print("new key:value:-",student["city"],"\n")

print("get() method:- Access the value in the dictionary(if key is missing the give none its not give error)")
print("Name:-",student.get("name"),"city:-",student.get("city","not found"),"state:-",student.get("state","not found"))
print("state:-",student.get("state","madhya pradesh"),"\n")

print("keys():-its gives all key only")
print(student.keys(),"\n")

print("values():- its gives all value only")
print(student.values(),"\n")

print("items():- its gives key:value in pairs")
print(student.items(),"\n")

print("pop() method:- its remove specified key:value from dictionary")
print("pop(age):-")
student.pop("age")
print(student.items(),"\n")

print("popitem() method:- its remove last inserted key:value accourding to modern python")
student.popitem()
print("after the popitem():-",student.items(),"\n")

print("update method:- update new value ya update new key:value")
student.update({"city":"bettiah","age":22,"roll_no":73})
print("after the update:-",student.items(),"\n")

print("copy() method:- its copy all data from previous dictionary")
student1=student.copy()
print("after the copy new dictionary student1:-",student1,"\n")

print("clear() method:- its clear all data from dictionary")
student1.clear()
print("after the clear student1:-",student1,"\n")

print("setdefault() method:- if key:value not found then add ithe dictonary")
student.setdefault("village","satbhirwa")
print(student,"\n")

print("fromkeys() method:- add multiple key same value")
keys=["name","age","city"]
data=dict.fromkeys(keys,None)
print(data,"\n")

print("In method:- check key is present in the dict if not then false otherwise True")
print("in:-(city)","city" in student,"\n")

print("not in method:-check key is present then false otherwise true")
print("not in:-(city)","city"not in student,"\n")




print(">>>>>>for loop in dictonary>>>>>")
print("in for loop dictonary name give only key:-")
for i in student:
    print(i)
print()
print("in for loop dictonary name.values give only key")

for i in student.values():
    print(i)
print()
print("i for loop dictonary name.items() give key&value both:-")
for i,j in student.items():
    print(i,j)
print()


print(".......nested loop in dictonary.......")
print("nested loop mean two dictonary in under the one dictonary ")

data={"data1":{"name":"vivek","city":"bhopal"},"data2":{"name":"rahul","city":"bettiah"}}
print(data["data1"])
print(data["data1"]["name"])
print(data["data2"])
print(data["data2"]["name"])