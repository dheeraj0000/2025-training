'''
def fib(n):
    if n<0:
        print("Incorrect Input")
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(int(input())))


                 "Dynamic programming"
'''                
fibval=[0,1]
def fib(n):
    if n<0:
        print("Incorrect number")
    elif n<len(fibval):
        return fibval[n]
    fibval.append(fib(n-1)+fib(n-2))
    return fibval[n]
print(fib(int(input())))

