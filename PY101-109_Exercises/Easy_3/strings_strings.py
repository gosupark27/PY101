def stringy(num):
    bin_lst = ['1','0'] * (num // 2)
    if num % 2 != 0:
        bin_lst.append('1')
    return "".join(bin_lst)

# You can append strings. Try it using that approach 

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True