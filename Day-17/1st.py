#consider two list  find the total sum of two list by adding list1 and reverse of list2
#list1=23 56 2 7 9 3
#list2=2 4 9 6 7 4

#res=[10,12,8,16,13,5]

l1=[6,5,2,7,9,3]
l2=[2,4,9,6,7,4]
res=[]
def ressum(left,right):
    if left==len(l1) and right==-1:
        return
    res.append(l1[left]+l2[right])
    ressum(left+1,right-1)
ressum(0,len(l2)-1)
print(res)

    
    
    

