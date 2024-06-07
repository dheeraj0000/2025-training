for i in range(int(input())):
    N=int(input())
    c=list(map(int,input().split()))
    totsum=c[0]
    totTime=0
    for i in c[1:]:
        totsum+=1
        totTime+=totsum
    print(totTime)