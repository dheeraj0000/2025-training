n,m=map(int,input().split())
f=list(map(int,input().split()))
print(abs(min(f[:n])-max(f[:n])))
