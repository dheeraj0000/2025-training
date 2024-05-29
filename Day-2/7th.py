#write a python program to remove all consective duplicates from a given string

n=str(input("enter string:"))
result = ""
pre = None
for char in n:
  if char != pre:
    result += char
  pre = char
print(result)