p1=input()
p2=input()
p3=input()
v=['a','e','i','o','u']
halku=[5,7,5]
res=[]
for i in (p1,p2,p3):
    count=0
    for c in i:
        if c in v:
            count+=1
    res.append(count)
if res == halku:
    print("yes")
else:
    print("No")
            