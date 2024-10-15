def power_to_n(base, power):
    result = 1
    for _ in range(0, power, 2):
        result *= multiply(base, base)
    return result if power % 2 == 0 else result // base

# Refined version of power_to_n(), thanks chatGPT 
def power_to_n(base, power):
    result = 1

    # Adjust for odd exponents
    if power % 2 != 0: 
        result = base
        power -= 1
    
    
    for _ in range(power // 2):
        result *= multiply(base, base)
    
    return result

def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = multiply(result, base)

    return result

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # Truepyt
# print(power_to_n(2,0) == 1)
# print(power_to_n(2,1) == 2)
# print(power_to_n(2,2) == 4)
# print(power_to_n(2,3) == 8)
# print(power_to_n(2,4) == 16)
# print(power_to_n(2,5) == 32)
# print(power_to_n(2,6) == 64)
# print(power_to_n(2,10) == 1024)
# print(power_to_n(3,7) == 2187)