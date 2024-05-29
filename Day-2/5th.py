#if data is number or not
import string
strNum=input()
for i in strNum:
  if i not in string.digits:
    print("False")
    break
else:
  print("True")