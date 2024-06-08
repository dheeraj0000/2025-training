def reverseWords():
    s = input("Enter a string: ")
    r = ' '.join(reversed(s.split()))
    print(r)

reverseWords()
