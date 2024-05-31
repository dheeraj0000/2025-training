#program to print sum of all odd numbers present in large number
#3446877846445566

n=int(input())
totSum=0
while n !=0:
  rem=n%10
  if rem%2!=0:
    totSum+=rem
  n//=10  
print(totSum)