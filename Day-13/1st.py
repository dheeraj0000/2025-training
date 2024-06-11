'''
sum of all the elements in array using recursion

INput: 15 2 6 12 8 5
output: 49
'''

def sum_array(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + sum_array(arr, index + 1)
arr = [1, 2, 3, 4, 5]
result = sum_array(arr)
print(f"The sum of the array is: {result}")