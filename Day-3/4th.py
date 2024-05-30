'''
write a python program to get a list sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
sample List:[(2,5),(1,2),(4,4),(2,3),(2,1)]
excepted result:[(2,1),(1,2),(2,3),(4,4),(2,5)]
'''

# Sample list of non-empty tuples
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sorting the list by the last element of each tuple
sorted_list = sorted(sample_list, key=lambda x: x[-1])

# Printing the sorted list
print(sorted_list)
