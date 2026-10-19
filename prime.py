
n = int(input("\nenter the number:- "))
def is_prime(n):
  if n <= 1:
    return False
  if n <= 3:
   return True
  if n%2==0 or n%3==0 :
   return False
  i=5
  while i*i<=n:
    if n%i==0 or n%(i+2)==0:
      return False
    i+=6
  return True
if is_prime(n):
  print("\n",n,"is a prime number\n")
else:
  print("\n",n,"is not a prime number\n")
  print("\tThank_You for using this program\n")
print("are you find the squre of any number:- (yes/no)")
choice=input()

if choice=="yes":
  num=int(input("enter the number:- "))
  square=num**2
  print("the squre is :-",square)
