'''
Input a list sort the elements in the list based on its:
input format
read the list
output format
sort the list accordting to the length of the eleements in the list
test cases
sample input : hi 1 425 2104              sample output: ['1','hi','425','2104']
sample input : 47 5102 0 abc                             ['47','5102','0','abc']
'''

dataList=input().split()
print(sorted(dataList,key=len))
