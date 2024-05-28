'''
data = "Hello Everyone"
odd_indexed_chars = data[1::2]
print(odd_indexed_chars)
'''


data = "Hello Everyone"
odd_indexed = [data[i] for i in range(1, len(data), 2)]
print(odd_indexed)
    