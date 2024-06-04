from collections import deque
class RecentCounter:
    def __init__(self):
      self.requests = deque()
    def ping(self,t:int)->int:    
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        self.requests.append(t)
        return len(self.requests)    

recentCounter = RecentCounter()
print(recentCounter.ping(1))    
print(recentCounter.ping(100))  
print(recentCounter.ping(3001)) 
print(recentCounter.ping(3002)) 
print(recentCounter.ping(3003))