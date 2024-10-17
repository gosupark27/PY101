def crunch(string):
    if len(string) < 2:
        return string
    non_duplicate_chars = []
    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            non_duplicate_chars.append(string[i])
    non_duplicate_chars.append(string[len(string) - 1])
    return "".join(non_duplicate_chars)


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee'))
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')