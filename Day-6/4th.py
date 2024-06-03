from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        resStack = []
        for op in operations:
            if op == 'D':
                resStack.append(2 * resStack[-1])
            elif op == '+':
                resStack.append(resStack[-1] + resStack[-2])
            elif op == 'C':
                resStack.pop()
            else:
                resStack.append(int(op))
        return sum(resStack)

s = Solution()
print(s.calPoints(['5', '2', 'C', 'D', '+']))
