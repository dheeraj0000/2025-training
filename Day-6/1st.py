'''
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def is_empty(self):
        return len(self.items) == 0
def is_palindrome(s):
    stack = Stack()
    # Push all characters of the string onto the stack
    for char in s:
        stack.push(char)
    # Pop characters from the stack and compare with the original string
    for char in s:
        if char != stack.pop():
            return False
    return True
# Read input from the user
user_input = input("Enter a string to check if it is a palindrome: ")
# Check if the input string is a palindrome
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
    
'''
strdata=input()
stack=list(strdata)
print(stack)
for i in strdata:
    if stack.pop()!=i:
        print("Not a palindrome")
        break
else:
    print("palindrome")
