#codeforces 460C
def max_height_of_smallest_flower(n, m, w, heights):
    max_growth = float('-inf')

    # Iterate through each flower as starting point of watering
    for i in range(n):
        total_height = 0

        # Calculate the sum of heights of flowers within the watering area
        for j in range(w):
            if i + j < n:  # Ensure we stay within the bounds of the flowers
                total_height += heights[i + j]

        # Update the maximum growth achieved
        max_growth = max(max_growth, total_height)

    return max_growth

# Input reading
n, m, w = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and output the maximum final height of the smallest flower
print(max_height_of_smallest_flower(n, m, w, heights))