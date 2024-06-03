def next_greater_number(digits):
    n = len(digits)
    i = n - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return -1
    
    j = n - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    digits[i], digits[j] = digits[j], digits[i]
    digits = digits[:i + 1] + digits[i + 1:][::-1]
    
    return ''.join(map(str, digits))
t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    digits = list(map(int, input().strip().split()))
    result = next_greater_number(digits)
    results.append(result)

for res in results:
    print(res)