def oddities(lst):
    odd_list = []
    index = 0
    while index < len(lst):
        if index % 2 == 0:
           odd_list.append(lst[index])
        index += 1

    return odd_list

# def oddities(lst):
#     return [num for index, num in enumerate(lst)
#                 if index % 2 == 0]


# print(oddities([2, 3, 4, 5, 6])) 
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True