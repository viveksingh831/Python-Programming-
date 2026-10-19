print("\n......STAR PATTERN........")

num=int(input("enter the range:- "))
for i in range (num):
    for j in range (num):
       print("*",end=" ")
    print()
print("Are you print othe type of pattern:- (yes/no)")
choice=input()
if choice=="yes":
    num=int(input("enter the range:- "))
    for i in range (num):
        for j in range (i+1):
          print("*",end=" ")
        print()