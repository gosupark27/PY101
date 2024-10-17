def century(year):
    if year < 101: 
        return '1st'
    new_century = True if year % 100 != 0 else False 
    century_number = (year // 100) + 1 if new_century else year // 100 
    match century_number:
        case 3:
            return str(century_number) + 'rd'
        case 11:
            return str(century_number) + 'th'
        case 12:
            return str(century_number) + 'th'
        case num if num % 10**(len(str(num)) - 1) == 1:
            return str(century_number) + 'st'
        case num if num % 10**(len(str(num)) - 1) == 2:
            return str(century_number) + 'nd'
        case _:
            return str(century_number) + 'th'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

# 4 digits: first 2 = century number, last 2 = keep or increment 
# digits: first digit = century number, last 2 
# 1 = fir st
# 2 = seco nd
# 3 = thi rd
# 4 = four th 
# 5 = fif th 
# 6 = six th 
# 7 = seven th 
# 8 = eigh th 
# 9 = nine th 
# 10 = ten th 
# 11 = eleven th 
# 12 = twleve th 
# 13 - 19 = th 
# 21 = twenty fir st 