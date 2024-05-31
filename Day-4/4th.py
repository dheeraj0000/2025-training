#Remove a given string keeping its special character at the same place
#input:h@ello
#output:o@lleh

'''
def reverse_string_preserving_special_chars(s):
    letters = [c for c in s if c.isalpha()]
    letters.reverse()
    result = []
    letters_iter = iter(letters)
    for c in s:
        if c.isalpha():
            result.append(next(letters_iter))
        else:
            result.append(c)
    return ''.join(result)

input_str = "h@ello"
output_str = reverse_string_preserving_special_chars(input_str)
print(output_str)  
'''



import re
string=input()
string_list=re.findall("[a-zA-Z]",string)
string_list.reverse()
for i in range(len(string)):
    if(string[i]=="#" or string[i]=='@'):
        string_list.insert(i,string[i])
print(''.join(string_list))

