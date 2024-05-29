from collections import deque


data = input().strip()
qstr = deque(input().strip())
rot = int(input().strip())
res = ''


for i in range(rot):
    di, mag = input().split()
    mag = int(mag)
    if di.lower() == 'l':
        qstr.rotate(-mag)  
    elif di.lower() == 'r':
        qstr.rotate(mag)  
    res += qstr[0]


subList = [data[i:i+rot] for i in range(len(data)-rot+1)]


for suble in subList:
    if sorted(suble) == sorted(res):
        print("yes")
        break
else:
    print("no")