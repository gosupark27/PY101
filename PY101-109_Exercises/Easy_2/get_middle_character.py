def center_of(string):
    even_length = True if len(string) % 2 == 0 else False
    if len(string) < 2:
        return string
    center = len(string) // 2
    return string[center:center + 1] if not even_length else string[center - 1:center + 1]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True