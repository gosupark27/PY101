# EXERCISE 1 #
# numbers = [1, 2, 3]
# numbers[6] = 5

# Will raises an out of bound error because the index is out of the range of the list 

# EXERCISE 2 #
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# def check_string_exclamation_mark(msg):
#     return msg.endswith('!')

# print(check_string_exclamation_mark(str1))
# print(check_string_exclamation_mark(str2))

# EXERCISE 3 #
# famous_words = "seven years ago..."

# new_str1 = "Four score and " + famous_words
# new_str2 = f'Four score and {famous_words}'

# print(new_str1)
# print(new_str2)

# EXERCISE 4 #
# munsters_description = "the Munsters are CREEPY and Spooky."
# # => 'The munsters are creepy and spooky.'
# new_msg = munsters_description.capitalize()
# new_msg = munsters_description[0].upper() + munsters_description[1::].lower()
# print(new_msg)

# EXERCISE 5 #
# munsters_description = "The Munsters are creepy and spooky."
# => "tHE mUNSTERS ARE CREEPY AND SPOOKY."
# print(munsters_description.swapcase())
# def reverse_case(msg):
#     reverse_str = ""
#     for letter in msg:
#         if letter.islower():
#             reverse_str += letter.upper()
#         else:
#             reverse_str += letter.lower()
#     return reverse_str

# print(reverse_case(munsters_description))

# EXERCISE 6 #
# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print('Dino' in str1)
# print('Dino' in str2)

# print('Dino appears') if str1.find('Dino') != -1 else print('NO DINO')
# print('Dino appears') if str2.find('Dino') != -1 else print('NO DINO')

# EXERCISE 7 #
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# print(flintstones)

# EXERCISE 8 #
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.extend(['Dino', 'Hoppy'])
# print(flintstones)

# EXERCISE 9 #
# advice = "Few things in life are as important as house training your pet dinosaur."
# # Expected output:
# # Few things in life are as important as
# index = advice.index('house')
# # print(advice[:index])
# print(advice.split("house")[0])

# EXERCISE 10 #
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))