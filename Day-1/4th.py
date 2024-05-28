a=list(map(str,input().split()))
f_num=a[0]
l_num=a[-1]
t=a[0]
a[0]=a[-1]
a[-1]=t
print(a)

'''
a=input().split()
a[0],a[-1]=a[-1],a[0]
print(a)
'''