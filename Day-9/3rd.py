n,t=map(int,input().split())
s=list(input().strip())
for i in range(t):
    i=0
    while i<n-1:
    
        if s[i]=='B' or s[i]=='b':
           s[i],s[i+1]=s[i+1],s[i]
           i+=1
        i+=1
print("".join(s))
   