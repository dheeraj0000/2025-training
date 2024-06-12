'''
def permuatation(s):
    n=len(s)
    low=0
    high=n
    n=input()
    for char in s:
        if s[i]=='I':
            append.perm(low)
        if s[i]=='D':
            append.perm(high)
 '''
'''
def reconstruct_permutation(s):
    n = len(s)
    low, high = 0, n
    perm = []

    for char in s:
        if char == 'I':
            perm.append(low)
            low += 1
        else:  
            perm.append(high)
            high -= 1
    perm.append(low)  

    return perm

s = "IDID"
print(reconstruct_permutation(s))

'''

def reconstruct_permutation(s):
    n = len(s)
    low, high = 0, n
    perm = []

    for char in s:
        if char == 'I':
            perm.append(low)
            low += 1
        else:  
            perm.append(high)
            high -= 1
    perm.append(low)  

    return perm

def main():
    # Take input for the string s
    s = input("Enter the string s (consisting of 'I' and 'D' characters): ")
    
    # Validate input
    if not all(char in 'ID' for char in s):
        print("Invalid input. The string should only contain 'I' and 'D' characters.")
        return
    
    # Generate the permutation
    result = reconstruct_permutation(s)
    
    # Print the resulting permutation
    print("The resulting permutation is:", result)

if __name__ == "__main__":
    main()



            
            
