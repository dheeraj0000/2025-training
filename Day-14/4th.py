def find_difference(nums):
    n = len(nums)
    
    # Initialize leftSum and rightSum arrays with zeros
    leftSum = [0] * n
    rightSum = [0] * n
    answer = [0] * n
    
    # Calculate leftSum
    for i in range(1, n):
        leftSum[i] = leftSum[i - 1] + nums[i - 1]
    
    # Calculate rightSum
    for i in range(n - 2, -1, -1):
        rightSum[i] = rightSum[i + 1] + nums[i + 1]
    
    # Calculate answer
    for i in range(n):
        answer[i] = abs(leftSum[i] - rightSum[i])
    
    return answer

# Dynamic input from user
def main():
    nums = []
    n = int(input("Enter the number of elements in the array: "))
    for i in range(n):
        num = int(input(f"Enter element {i + 1}: "))
        nums.append(num)
    
    result = find_difference(nums)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()
