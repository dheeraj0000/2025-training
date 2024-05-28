cubes=[]
for i in range(1,6):
    c=i*i*i
    if c%2==0:
        cubes.append(c)
print(cubes)

'''
cubeList=[i*i*i for i in range(1,6) if i*i*i %2==0]
print(cubeList)
'''