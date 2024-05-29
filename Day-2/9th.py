# taking a word and performing rotation then finding anagram or not 

data=input()
rot=int(input())
res=''
for i in range(rot):
  di,mag=input().split()
  if di.upper=='L':
    (data[mag:]+data[:int(mag)])
  elif di.upper()=="R":
    res+=(data[:int(mag)]+data[int(mag)])
subList=[data[i:i+rot] for i in range(len(data))]
for subele in subList:
  if sorted(subele)==sorted(res):
    print("Yes")
    break
else:
  print("No")