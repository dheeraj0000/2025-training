#self sufficient
N=int(input())
eList=list(map(int,input().split()))
cList=list(map(int,input().split()))
cost=sum(eList)-sum(cList)
if cost<0:
    print(abs(cost))
else:
    print("0")
    