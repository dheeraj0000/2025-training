'''
N,k=map(int,input().split())
for deno in range(N,0,-1):
    if N%deno==0:
        k-=1
    if k==0:
        print(deno)
        break
if k!=0:
    print("1")

'''

