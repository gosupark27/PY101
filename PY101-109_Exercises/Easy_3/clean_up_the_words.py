# Can do everything in one for loop. Checking previous char is the right logic

def clean_up(string):
    if len(string) == 0:
        return ''
    elif len(string) == 1:
        return string if string.isalpha() else ' '
    
    result = ""

    for i, c in enumerate(string): 
        if not c.isalpha():
            result += ' '
        else:
            result += c
    
    new_result = result[0]
    for i, c in enumerate(result): 
        if i > 0 and (result[i - 1] != result[i]):
            new_result += result[i]
    return new_result

print(clean_up("---what's my +*& line?") == " what s my line ")
# True

# traverse the string 
# check if char is alpha 
# if non-alpha check if previous char is whitespace
# if whitespace don't do anything, if not then add whitespace

