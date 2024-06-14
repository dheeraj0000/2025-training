def recReverse(dList,left,right):
    if left>right:
        return dList
    dList[left],dList[right]=dList[right],dList[left]
    return recReverse(dList,left+1,right-1)

n1=[7,9,4,3,2]
n2=[6,8,10,4,14,6]
n=len(n1)
print(recReverse(n1,0,n-1))
n=len(n2)
print(recReverse(n2,0,n-1))