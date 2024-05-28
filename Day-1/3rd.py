'''
d='12653'
dlist=list(data)
print(sorted(dlist))
'''

d=int(input())
r=[str(i) for i in range(1,d+1)]
r.sort()
print(list(map(int,r)))