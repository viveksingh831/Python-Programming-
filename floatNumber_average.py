print("enter how many numbers to calculate average")
n = int(input())
sum = 0
print("enter the",n,"float numbers")
for i in range (n):
 num = float(input())
 sum += num
average = sum/n
print("the average of floating number of",average)