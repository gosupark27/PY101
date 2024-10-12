SQ_M_TO_SQ_FT = 10.7639
isMetric = None

def main(): 
    dimensions = get_user_inputs()
    areas = calc_area(dimensions[0], dimensions[1])
    print_results(areas[0], areas[1])

def get_user_inputs():
    global isMetric
    isMetric = True if 'y' == input("Is the measurement type in meters? (y/n):").lower() else False
    length = float(input(f"What is the length of the room (in {'meters' if isMetric else 'feet'}): "))
    width = float(input(f"What is the width of the room (in {'meters' if isMetric else 'feet'}): "))
    return length, width

def calc_area(length, width):
    square_meters = length * width if isMetric else (length * width) / SQ_M_TO_SQ_FT
    square_feet = square_meters * SQ_M_TO_SQ_FT if isMetric else length * width
    return square_meters, square_feet

def print_results(square_meters, square_feet):
    room_area = f'{square_meters:.2f}' if isMetric else f'{square_feet:.2f}'
    room_area_conversion = f'{square_meters:.2f} square meters' if not isMetric else f'{square_feet:.2f} square feet'
    print(f'The area of the room is {room_area} {'meters' if isMetric else 'feet'} squared ({room_area_conversion})')

main()