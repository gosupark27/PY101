def short_long_short(str1, str2):
    return str1 + str2 + str1 if len(str1) < len(str2) else str2 + str1 + str2
    
# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

# Great solution by Cora
def short_long_short(str1, str2):
    sorted_strs = sorted([str1, str2], key=len)
    return sorted_strs[0] + sorted_strs[1] + sorted_strs[0]