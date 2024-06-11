#prime number or not using recursion
'''
num=17
for deno in range(2,int(num**0.5)+1):
    if num%deno==0:
        print("false")
    else:
        print("true")
'''      
        
n = int(input())

def isprime(n, deno=2):
    if n < 2:
        return False
    if deno > int(n**0.5):
        return True
    if n % deno == 0:
        return False
    return isprime(n, deno + 1)

print(isprime(n))
