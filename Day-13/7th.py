'''
Find the gcd of a number
find the gcd of two number
check whether two numbers are co-prime or not
'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
num1 = 48
num2 = 18
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
