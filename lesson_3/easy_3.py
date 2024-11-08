# EXERCISE 1 #
# numbers = [1, 2, 3, 4]

# # numbers.clear()

# while numbers:
#     numbers.pop()
# print(numbers)

# EXERCISE 2 #
# print([1, 2, 3] + [4, 5])

# prints [1, 2, 3, 4, 5]

# EXERCISE 3 #
# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)

# prints "hello there" 

# EXERCISE 4 #
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# prints [{"first": 42}, ...] because of shallow copy nested dict are stored as reference 

# EXERCISE 5 #
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

def color_valid1(color):
    return color == "blue" or color == "green"

def color_valid2(color):
    return color in ["blue", "green"]

print(color_valid1('blue'))
print(color_valid2('green'))
print(color_valid1('black'))
print(color_valid2('grey'))