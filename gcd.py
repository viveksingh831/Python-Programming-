print("\n\n.......GCD.......\n")
number=list(map(int,input("\nenter the numbers:- ").split()))
def get_gcd(x,y):
    while y!=0:
        x,y=y,x%y
        
    return x
ans=number[0]
for i in number[1:]:
    ans=get_gcd(ans,i)
print("the greatest common factor is:-",ans,"\n\n") 
print("are you want to find the lcm  (yes/no)")

choice=input()
if choice=="yes":
 print("same input type 's' or otherwise 'n' for new input")
else:
   print("are you want to find the average:- (yes/no)")
   choice=input()
   if choice=="yes":
     print(".......Average.......\n")
     print("same input type 's' or otherwise 'n' for new input")
     if choice=="s":
      avg=sum(number)/len(number)
      print("the average is :- ",avg) 
     elif choice=="N or n":
      number=list(map(int,input("enter the numbers:- ").split()))
      print(".......Average.......\n")
      avg=sum(number)/len(number)
      print("the average is :- ",avg,"\n\n")
   else:
      print("are you want to find factorial:- (yes/no)")
      choice=input()
      if choice=="yes":
        print(".......Factorial.......\n")
        n=int(input("enter the number:-"))
        fact=1
        for i in range(1,n+1):
            fact*=i
        print("the factorial is :- ",fact)
      else:
        print("Thank_You for using this program\n")

choice=input()
if choice=="s":
 print(".......LCM.......\n")
 def get_lcm(x,y):
      lcm=(x*y)//get_gcd(x,y)
      return lcm
 ans=number[0]
 for i in number[1:]:
    ans=get_lcm(ans,i)
 print("the least common multiple is:-",ans,"\n\n")

elif choice=="n":
    number=list(map(int,input("enter the numbers:- ").split()))
    print(".......LCM.......\n")
    def get_lcm(x,y):
      lcm=(x*y)//get_gcd(x,y)
      return lcm
    ans=number[0]
    for i in number[1:]:
        ans=get_lcm(ans,i)
    print("the least common multiple is:-",ans,"\n\n")