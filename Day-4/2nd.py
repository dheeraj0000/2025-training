#program to sort first half in ascending order and second half in descending order in an array
#input: 1 21 5 2 50 16
#output : 1 2 5 50 21 16

numList=list(map(int,input().split()))
n=len(numList)
res=sorted(numList)[:n//2]
res+=sorted(numList,reverse=True)[:n//2+1]
print(res)