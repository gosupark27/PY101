def triangle(n):
    for row in range(n):
        line = ''
        for col in range(n):
            if n - row - 1 <= col:
                line += '*'
            else:
                line += ' '
        print(line)

# It is possible to do this with one for loop instead of nested for loops; 
# Also, make use of * operator ! 

triangle(5)
triangle(9)