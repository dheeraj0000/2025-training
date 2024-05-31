#Police Recruits

'''
a=int(input())
l=list(map(int,input().split()))
b=[]
c=[]
if l[n]==1&&-1:
    l.append(b)
else l[n]==-1:
    l.append(c)
 '''

'''
n=int(input())
l1=list(map(int,input().split()))
crimes=0
while n!=0:
  if l1[n]==1 and l1[i+1]==-1:
    crimes=0
  elif l1[i]==-1 and l1[i-1]==1 or l1[i-1]==0:
    crimes+=1
  else:
    crimes=0
print(crimes)
'''


num=int(input())
events=list(map(int,input().split()))
a=0
c=0
for event in events:
    if event>0:
        a+=event
    elif event==-1:
        if a <= abs(event):
            c+=abs(event)-a
            a=0
        else:
            a-=abs(event)
print(c)
      
            
