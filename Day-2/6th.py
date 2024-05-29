#generate a number from the given string digit found 0 
#123av45b78                1234578

def generate(s):
    result=" "
    for char in s:
        if char.isdigit():
            result+=char
    if result=="":
        return 0
    return int(result)

str="123av45b78"
print(generate(str))

