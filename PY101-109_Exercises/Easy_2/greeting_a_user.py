def greetings(name):
    normal_greeting = f'Hello {name}.'
    loud_greeting = f'hello {name} why are we yelling?'.upper()
    return loud_greeting if '!' in name else normal_greeting

name = input("What is your name? ")
print(greetings(name))