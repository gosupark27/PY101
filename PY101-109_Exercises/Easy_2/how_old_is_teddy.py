import random as r 

def print_age():
    age = r.randint(20, 100)
    return f'Teddy is {age} years old!'

print(print_age())