def print_in_box(msg):
    horizontal = f'+-{'-' * len(msg)}-+'
    vertical = f'| {' ' * len(msg)} |'



    print(f'{horizontal}\n{vertical}\n{f'| {msg} |'}\n{vertical}\n{horizontal}')

print_in_box('hello')
print_in_box('To boldly go where no one has gone before.')
print_in_box('')