from datetime import datetime as dt

def get_input():
    age = int(input("What is your age? "))
    retire_age = int(input("At what age would you like to retire? "))
    return age, retire_age

def result():
    age, retire_age = get_input()
    current_year = dt.today().year
    years_left = retire_age - age
    return (f"It's {current_year}. You will retire in {current_year + years_left}." + 
            f"\nYou have only {years_left} years of work to go!")

print(result())