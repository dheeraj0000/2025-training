'''
palindrome of a number or not using recursion

input: 1221 output:true
input: 12210  output:false
'''


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
n=input()
print(is_palindrome(n))  
 