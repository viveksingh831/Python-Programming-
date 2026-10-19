import re


print("Do tou want to find the greater number through function:- (yes/no)")
choice=input()
if choice=="yes":
    def greater(*numbers):
        return (max(numbers))
    numbers=map(int,input("enter the numbers:- ").split())
    print(greater(*numbers)," is the greatest number")# *args= multiple argument 
else:
    print("Do you want to find sum of even number:- (yes/no)")
    choice=input()
    if choice=="yes":
        def even_sum(*numbers):
            total=0
            for i in numbers:
                if i%2==0:
                    total +=i
            return total
        numbers=map(int,input("enter the numbers:-").split())
        print(even_sum(*numbers))
print("Do you want to check palindrome number:- (yes/n")
choice=input()
if choice=="yes":
    def palindrome(number):
        rev=0
        while number>0:
            rem= number%10
            rev=rev*10+rem
            number=number//10
        return rev
    number=int(input("enter the number:- "))
    if palindrome(number)==number:
        print("Yes the given number is palindrome number\nBecause:- ",number,"=",palindrome(number))  
    else:
        print("No the given number is not a palindrome number\nBecause:- ",number,"!=",palindrome(number))
else:
    print("Do you want to find my address:- (yes/no)")
    choice=input()
    if choice=="yes":
        
        def vivek(**Address):# **kwargs= multiple string
            for key,value in Address.items():
                print(key,"=",value)
        vivek(Name="vivek",Village="Satbhirwa",City="Majhauliya",
                    Post="majhauliya",Police_Station="Majhauliya",District="west_Champaran Bettiah",
                    Mobile="7488584033")
    else:
        print("do you want to convert string into captial/small:- ")
        choice=input()
        if choice=="yes":
            text=input("enter the strings:-")
            print("captial/small:-")
            choice =input()
            if choice=="captial":
                print(text.upper())
            else:
                print(text.lower())
                                    
                
"""def vivek(a,b):
    sum= a+b
    print(sum)
print(vivek(5,6))"""


    

              

    
    
    
    

