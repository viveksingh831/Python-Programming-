print("\n👉🏻Enter 4 numbers to check which is greater")

num1 = int(input("👉🏻Enter first number  :- "))
num2 = int(input("👉🏻Enter secound number:- "))
num3 = int(input("👉🏻Enter third number  :- "))
num4 = int(input("👉🏻Enter fourth number :- "))

if(num1 > num2 and num1 >num3 and num1 > num4):
    print("\n👉🏻1st greater number is:-",num1)
    if(num2 > num3 and num2 > num4):
        print("\n👉🏻2nd greater number is:-",num2)
        if(num3 > num4):
            print("\n👉🏻3rd greater number is:-",num3)
            print("\n👉🏻The lowest number is:-",num4,"\n")  
        else:
            print("\n👉🏻3rd greater number is:-",num4)
            print("\n👉🏻The lowest number is:-",num3,"\n")

    elif(num3 > num2 and num3 > num4):
        print("\n👉🏻2nd greater number is:-",num3)
        if(num2 > num4):
            print("\n👉🏻3rd greater number is:-",num2)
            print("\n👉🏻The lowest number is:-",num4,"\n")   
        else:
            print("\n👉🏻3rd greater number is:-",num4)
            print("\n👉🏻The lowest number is:-",num2,"\n")    
    else:
        print("\n👉🏻2nd greater number is:-",num4)
        if(num2 > num3):
            print("\n👉🏻3rd greater number is:-",num2)
            print("\n👉🏻The lowest number is:-",num3,"\n")  
        else:
            print("\n👉🏻3rd greater number is:-",num3)  
            print("\n👉🏻The lowest number is:-",num2,"\n")  



elif(num2 > num3 and num2 > num4):
    print("\n👉🏻1st greater number is:-",num2)
    if(num3 > num4 and num3 > num1):
        print("\n👉🏻2nd greater number is:-",num3)
        if(num4 > num1):
            print("\n👉🏻3rd greater number is:-",num4)
            print("\n👉🏻The lowest number is:-",num1,"\n")
        else:
            print("\n👉🏻3rd greater number is:-",num1)
            print("\n👉🏻The lowest number is:-",num4,"\n")  

    elif(num4 > num3 and num4 > num1):
        print("\n👉🏻2nd greater number is :-",num4)
        if(num3 > num1):
            print("\n👉🏻3rd greater number is:-",num3)
            print("\n👉🏻The lowest number is:-",num1,"\n")  
        else:
            print("\n👉🏻3rd greater number is:-",num1)
            print("\n👉🏻The lowest number is:-",num3,"\n")
    else:
        print("\n👉🏻2nd greater number is:-",num1) 
        if(num3 >num4):
            print("\n👉🏻3rd greater number is:-",num3)
            print("\n👉🏻The lowest number is:-",num4,"\n")

             
elif(num3 >num4):
    print("\n👉🏻1st greater number is:-",num3)
    if(num4 > num1 and num4 > num2 ):
        print("\n👉🏻2nd greater number is:-",num4)
        if(num1 > num2):
            print("\n👉🏻3rd greater number is:-",num1)
            print("\n👉🏻The lowest number is:-",num2,"\n")
    elif(num1 > num2 and num1 > num4 ): 
        print("\n👉🏻2nd greater number is:-",num1)
        if(num4 > num2):
            print("\n👉🏻3rd greater number is:-",num4)
            print("\n👉🏻The lowest number is:-",num2,"\n")
        else:
            print("\n👉🏻3rd greater number is:-",num2)
            print("\n👉🏻The lowest number is:-",num4,"\n")

    else:
        print("\n👉🏻2nd greater number is:-",num2) 
        if(num1 > num4):
            print("\n👉🏻3rd greater number is:-",num1)
            print("\n👉🏻The lowest number is:-",num4,"\n") 


           
else:
    print("\n👉🏻1st greater number is:-",num4)
    if(num1 > num2 and num1 > num3 ):
        print("\n👉🏻2nd greater number is:-",num1)
        if(num2 > num3):
            print("\n👉🏻3rd greater number is:-",num2)
            print("\n👉🏻The lowest number is:-",num3,"\n")
    elif(num2 > num1 and num2 > num3 ):
        print("\n👉🏻2nd greater number is:-",num2)
        if(num1 > num3):
            print("\n👉🏻3rd greater number is:-",num1)
            print("\n👉🏻The lowest number is:-",num3,"\n")
    else:
        print("\n👉🏻2nd greater number is:-",num3) 
        if(num1 > num2):
            print("\n👉🏻3rd greater number is:-",num1)
            print("\n👉🏻The lowest number is:-",num2,"\n")
        else:
            print("\n👉🏻3rd greater number is:-",num2)
            print("\n👉🏻The lowest number is:-",num1,"\n")

                
print("\t🌹 🌹 ❤️❤️❤️ 🌹 🌹")

vivek1 = [1,3,4,6,5,7,]
vivek2 = (1,3,5,6,8,9,)
print(type(vivek1),vivek1)                      
            