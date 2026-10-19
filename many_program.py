print("Are you find the table of any number:- (yes/no)")
choice=input()
if choice=="yes":
    num=int(input("enter the number:- "))
    for i in range(1,11):
        table=num*i
        print(table,end=" ")
    print()
    print("Are you find fibonacci series of any number :- (yes/no)")
    choice=input()
    if choice=="yes":
        num=int(input("enter the range of fibonacci series:- "))
        a=0
        b=1
        print(a,b,end=" ")
        for i in range(2,num):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
    print("\nAre you find the power of any number:- (yes/no)")
    choice=input()
    if choice=="yes":
        num=int(input("enter the number:- "))
        num1=int(input("enter the power:- "))
        num**=num1
        print("The power is ",num)

else:
    print("Do you want to find the squre then palindrome of any number:- (yes/no)")
    choice=input()
    if choice=="yes":
        num1=int(input("enter the number:- "))
        num1**=2
        print("the squre is ",num1)
    

    else:
        print("Are you find cube of any number:- (yes/no)")
        choice=input()
        if choice=="yes":
            num2=int(input("enter the number:- "))
            
            num2**=3
            print("the cube is ",num2)

        else:
            print("Are you find sum of big number using floor division:- (yes/no)")
            choice=input()
            if choice=="yes":
               number=int(input("enter the number"))
               total=0
               while number>0:
                   digit=number%10
                   total +=digit
                   number=number//10

               print("The sum:- ",total)

            else:
                print('Do you want to find the reverse of a large number using floor division:- (yes/no)')
                choice=input()
                if choice=="yes":
                   number=int(input("enter the number:- "))
                   rev=0
                   while number>0:
                       digit=number%10
                       rev=rev*10+digit
                       number=number//10
                   print("The reverse is:- ",rev)
                else:
                    print("Do you want to find the count of digit of large number:- (yes/no)")
                    choice=input()
                    if choice=="yes":
                        number=int(input("enter the number:- "))
                        count=0
                        while number>0:
                            number=number//10
                            count +=1
                        print("The count is:- ",count)
print("Do you want to check the palindrome number:- (yes/no)")
choice=input()
if choice=="yes":
    number=int(input("enter the number:-"))
    original=number
    rev=0
    while number>0:
        digit=number%10
        rev=rev*10+digit
    
        number=number//10
    if original==rev:
        print("Yes given number is a palindrome number\nBecause:- ",original,"=",rev)
    else:
        print("No given number is not a palindrome number\nBecause:- ",original,"!=",rev)
else:
    print("Do you want to check the Armstrong number:- (yes/no)")
    choice=input()
    if choice=="yes":
        number =int(input("enter the number:- "))
        original=number
        sum=0
        while number>0:
            digit=number%10
            digit **=3
            sum +=digit
            number=number//10
        if original==sum:
            print("Yes given number is a Armstrong number\nBecause:- ",original,"=",sum)
        else:
            print("No given number is not a Armstrong number\nBecause:- ",original,"!=",sum)
        print("")
    else:
        print("Do you want to check strong number:- (yes/no)")
        choice=input()
        if choice=="yes":
            number=int(input("enter the number:-"))
            original=number
            sum=0
            while number>0:
             fact=1
             

             digit=number%10
             for i in range(1,digit+1):
                fact *=i
                
             sum +=fact
             number=number//10
            if original==sum:
                print("Yes the given number is a Strong number\nBecause:-",original,"=",sum)
            else:
                print("No the given number is not a Strong number\nBecause:-",original,"!=",sum)

            
                    















