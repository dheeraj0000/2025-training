import math
n=int(input())-1
m=int(input())-1
x=int(input())-1
y=int(input())-1
def validPath():
  total_path=math.factorial(n+m)//(math.factorial(n)*math.factorial(m))
  path_to_xy=math.factorial(x+y)//(math.factorial(x)*math.factorial(y))
  xy_to_mn=math.factorial(n-x+m-y)//(math.factorial(n-x)*math.factorial(m-y))
  return total_path-(path_to_xy*xy_to_mn)
print(validPath())