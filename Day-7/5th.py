from collections import deque

def longest_subarray(nums, limit):
    min_deque = deque()
    max_deque = deque()
    left = 0
    max_length = 0

    for right in range(len(nums)):
        while min_deque and min_deque[-1] > nums[right]:
            min_deque.pop()
        while max_deque and max_deque[-1] < nums[right]:
            max_deque.pop()  
        min_deque.append(nums[right])
        max_deque.append(nums[right])
        while max_deque[0] - min_deque[0] > limit:
            if min_deque[0] == nums[left]:
                min_deque.popleft()
            if max_deque[0] == nums[left]:
                max_deque.popleft()
            left += 1
        max_length = max(max_length, right - left + 1)
    
    return max_length
print(longest_subarray([8,2,4,7], 4))      
print(longest_subarray([10,1,2,4,7,2], 5)) 
print(longest_subarray([4,2,2,2,4,4,2,2], 0)) 
