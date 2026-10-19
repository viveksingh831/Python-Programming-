import math
a,b,c,d =map(int,input("enter 4 numbers:- ").split())
ans=math.gcd(a,b,c,d)
print("greatest common factor is:-",ans)
print()
number=map(int,input("enter the numbers:- ").split())
ans=math.gcd(*number)
print(ans)


number=list(map(int,input("enter the number:-").split()))
def get_gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
ans=number[0]
for i in number[1:]:
    ans=get_gcd(ans,i)

print(ans)