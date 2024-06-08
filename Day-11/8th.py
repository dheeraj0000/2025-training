#leetcode 1207
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        from collections import Counter
        count = Counter(arr)
        occurrences = set(count.values())
        return len(occurrences) == len(count)
solution = Solution()
print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # Output: True
print(solution.uniqueOccurrences([1, 2]))              # Output: False
print(solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # Output: True