
n=int(input())
flist=list(map(int,input().split()))
info={}
k=1
for i in flist:
    info[i-1]=k
    k+=1
#print(info.values())
for i in range(n):
    print(info[i],end=' ')


'''
def find_gift_givers(n, p):
    result = [0] * n                       
    for giver in range(n):
        receiver = p[giver]
        result[receiver - 1] = giver + 1
    return result


n = int(input())
p = list(map(int, input().split()))
result = find_gift_givers(n, p)
print(' '.join(map(str, result)))
'''