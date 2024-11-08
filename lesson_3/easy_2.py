# EXERCISE 1 #
# numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# # print(numbers[::-1])
# numbers.reverse()
# print(numbers)
# reversed_numbers = list(reversed(numbers))

# EXERCISE 2 #
# numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

# number1 = 8  # False (not in numbers)
# number2 = 95 # True (in numbers)

# print(number1 in numbers)
# print(number2 in numbers)

# EXERCISE 3 # 
# def check_num_within_range(val, start=10, end=100):
#     return val >= start and val <= end

# print(check_num_within_range(42))
# print(check_num_within_range(100))
# print(check_num_within_range(101))

# print(42 in range(10, 101))
# print(100 in range(10, 101))
# print(101 in range(10, 101))

# EXERCISE 4 #
# numbers = [1, 2, 3, 4, 5]
# # numbers.pop(2)
# # print(numbers)

# del numbers[2]
# print(numbers)

# EXERCISE 5 #
# numbers = [1, 2, 3, 4]
# table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# print(isinstance(numbers, list))
# print(isinstance(table, list))

# print(type(table).__name__, type(table) is list)
# print(type(numbers).__name__, type(numbers) is list)

# EXERCISE 6 #
# title = "Flintstone Family Members"
# # padding = (40 - len(title)) // 2
# # whitespace = " " * padding
# # new_title = whitespace + title + whitespace
# # print(new_title, len(new_title))

# print(title.center(40))

# EXERCISE 7 #
# statement1 = "The Flintstones Rock!"
# statement2 = "Easy come, easy go."

# print(statement1.count('t'))
# print(statement2.count('t'))

# EXERCISE 8 #
# ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
# print('Spot' in ages)

# EXERCISE 9 #
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)
print(ages)