'''
Display the largest palindrome from the given number
input:120021   output:120021
input:12210    output:1221
'''

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

data=input()
def largestpal():
    maxLen=0
    larpal=''
    for i in range(len(data)):
        for j in range(i+1,len(data)+1):
            substr=data[i:j]
            if is_palindrome(substr):
                if len(substr)>maxLen:
                    maxLen=len(substr)
                    larpal=substr
    return larpal
print(largestpal())