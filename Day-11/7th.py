'''
s=input()
l=len(s)
#print(l)
count=0
def string(s):
    if l!=26:
        print("false")
        break
    for i in range(s):
        if s[i]==s[j]:
            count+=1
        else:
            print("true")
            
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentences))==26

        
    