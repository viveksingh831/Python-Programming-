a,b,c,d,e = map(int,input("enter the 5 numbers:- ").split())
sum=a+b+c+d+e
ave=sum/5
mul=a*b*c*d*e
print(sum,"\n",ave,"\n",mul)
numbers=[a,b,c,d,e]
greater=numbers[0]
for n in numbers:
    if n>greater:
        greater=n
lowest=numbers[0]
for n in numbers:
   if n<lowest:
        lowest=n
print("greater number is:- ",greater,"\n","lowest number:- ",lowest)   