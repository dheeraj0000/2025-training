#1046  last stone weight
#leetcode 1046
import heapq

def lastStoneWeight(stones):
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)
        if first != second:
            heapq.heappush(max_heap, -(first - second))
    return -max_heap[0] if max_heap else 0

stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))  
stones = [1]
print(lastStoneWeight(stones))