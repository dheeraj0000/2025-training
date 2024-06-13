def canPlaceFlowers(flowerbed, n):
    count = 0
    length = len(flowerbed)
    
    for i in range(length):
        if flowerbed[i] == 0:
            # Check if the left and right plots are empty or out of bounds
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            if empty_left and empty_right:
                # Plant a flower here
                flowerbed[i] = 1
                count += 1
                
                # If we have planted enough flowers, return True
                if count >= n:
                    return True
    
    return count >= n

# Example usage:
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(canPlaceFlowers(flowerbed1, n1))  # Output: True

flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(canPlaceFlowers(flowerbed2, n2))  # Output: False