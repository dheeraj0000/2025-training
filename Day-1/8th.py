bList=list(map(int, input().split()))
count,maxVal=0,0
for i in bList:
    if i==1 :
        count+=1
        if count>maxVal:
            maxVal=count
        else:
            count=0
print(maxVal)