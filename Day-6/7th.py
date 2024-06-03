n=int(input())
t=list(map(int,input().split()))
side=[]
result=[]
for i in range(0,len(t)-1):
    if t[i]>t[i+1]:
        side.append(t[i])
    else:
        result.insert(0,t[i])
result.insert(0,t[-1])
resut=side+result
if sorted(t,reverse=True)==result:
    print("yes")
else:
    print("No")