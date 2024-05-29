'''
def des(num):
    if num == 0:  
        return    
    print(num, end=" ")  
    des(num - 1)  
user = int(input("Enter a number: "))
des(user)
'''


def des(num):
    if num == 0:  
        return    
    #print(num, end=" ")  
    des(num - 1)
    print(num, end=" ")  
user = int(input("Enter a number: "))
des(user)