'''
n=list(map(int,input().split()))

c=0

for i in range(n):
    for j in range(i+1):
        if s[i]==s[j] and i<j:
            c+=1
print(c)
'''
    

n = list(map(int, input().split()))

c = 0


for i in range(len(n)):
    for j in range(i + 1, len(n)):  
        if n[i] == n[j]:
            c += 1
            
print(c)
