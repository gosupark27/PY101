# Ask the user for the first number
# Ask the user for the second number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')

prompt("Enter the first number: ")
first_num = input()

while not invalid_number(first_num):
    prompt("Invalid input - enter a valid number: ")
    first_num = input()

prompt("Enter the second number: ")
second_num = input()

while not invalid_number(second_num):
    prompt("Invalid input - enter a valid number: ")
    second_num = input()

prompt("What operation would you like to perform:\n1) Add " +
                  "2) Subtract 3) Multiply 4) Divide\n")
operation = input()

while operation not in [1, 2, 3, 4]:
    prompt("What operation would you like to perform:\n1) Add " +
                  "2) Subtract 3) Multiply 4) Divide\n")
    operation = input()

first_num = int(first_num)
second_num = int(second_num)

match operation:
    case '1':
        output = f'{first_num} + {second_num} = {first_num + second_num}'
    case '2':
        output = f'{first_num} - {second_num} = {first_num - second_num}'
    case '3':
        output = f'{first_num} * {second_num} = {first_num * second_num}'
    case '4':
        output = f'{first_num} / {second_num} = {first_num / second_num}'

prompt(output)
