#shortest distance to a character    given a string s and a character c that occurs

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [float('inf')] * n

        # Left to right pass
        prev = float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            if prev != float('inf'):
                answer[i] = i - prev

        # Right to left pass
        prev = float('inf')
        for i in range(n-1, -1, -1):
            if s[i] == c:
                prev = i
            if prev != float('inf'):
                answer[i] = min(answer[i], prev - i)
        
        return answer