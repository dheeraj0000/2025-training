'power of 6 return true if not return false'

'''
num=int(input())
while num!=1:
    if num%6==0:
        num//=6
        print(num)
    else:
        print("false")
        break
else:
    print("true")
'''
    
def des(num):
    if num == 0:  
        return    
    print(num, end=" ")  
    des(num - 1)  
user = int(input("Enter a number: "))
des(user)
    
    
