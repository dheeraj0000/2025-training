'''
nList=[5,1,6]
def allSub():
    res=[[]]
    for i in range(len(nList)):
        for j in range(i+1,len(nList)+1):
            res.append(nList[i:j])
    return res
print(allSub())
'''

import itertools

mList = [5, 1, 6]
for i in range(len(mList) + 1):
    print(list(itertools.combinations(mList, i)))

