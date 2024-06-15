List1 = [6, 5, 2, 7, 9, 3]
List2 = [2, 4, 9, 6, 7, 4]
res = []
i=0
while i<len(List1):
    if List1[i]%2!=0:
        i+=1
        continue
    j=0
    while j<len(List2):
        if List2[j]%2!=0:
            res.append(List1[i]+List2[j])
            j+=1
            continue
        j+=1
    i+=1
print(res)