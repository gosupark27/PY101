def multisum(other_num):
    return sum([num for num in range(1, other_num + 1)
                    if num % 3 == 0 or num % 5 == 0])
    # Can use list comprehension like above or use a generator expression
    # to get the same result. 
    # return sum(num for num in range(1, other_num + 1)
    #                if num % 3 == 0 or num % 5 == 0)

# Using for loop
# def multisum(other_num):
#     multiples_3_5 = [num for num in range(1, other_num + 1)
#                          if num % 3 == 0 or num % 5 == 0]
#     sum = 0
#     for multiple in multiples_3_5:
#         sum += multiple
#     return sum

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)