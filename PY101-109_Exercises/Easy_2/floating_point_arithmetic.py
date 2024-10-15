def floating_point_arithmetic(num1, num2):
    operators = ['+', '-', '*', '/', '//', '%', '**']
    for op in operators:
        print(f'{num1} {op} {num2} = {eval(f'{num1}{op}{num2}')}')

first_num = float(input('Enter the first number: '))
second_num = float(input('Enter the second number: '))
floating_point_arithmetic(first_num, second_num)