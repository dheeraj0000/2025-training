

#Problem meatball
from collections import deque

def last_served_meatball_index(N, D, weights):
    queue = deque((weight, i + 1) for i, weight in enumerate(weights))
    
    last_served_index = -1
    
    while queue:
        weight, index = queue.popleft()
        if weight <= D:
         
            last_served_index = index
        else:
    
            queue.append((weight - D, index))
    
    return last_served_index


N = 4
D = 2
weights = [7, 8, 9, 3]
print(last_served_meatball_index(N, D, weights))  