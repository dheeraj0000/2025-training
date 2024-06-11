import math

def is_square_free(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % (i * i) == 0:
            return False
    return True

def count_square_free_divisors(num):
    square_free_count = 0
    
    for i in range(1, num + 1):
        if num % i == 0 and i != 1 and is_square_free(i):
            square_free_count += 1
    
    return square_free_count

# Example usage
num = 20
print(f"The number of square-free divisors of {num} is {count_square_free_divisors(num)}")