#print the string in reverse order using recursion


def revstring(data):
    if data=="":
        return data
    return data[-1]+revstring(data[:-1])

strData="why are you shy"
print(revstring(strData))
