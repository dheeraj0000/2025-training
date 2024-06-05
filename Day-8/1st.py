T = int(input("Enter :"))
for _ in range(T):
    P = input()
    S = input()
    small_lex = ""
    for char in P:  
        if char in S:
            small_lex += char
    print(small_lex)