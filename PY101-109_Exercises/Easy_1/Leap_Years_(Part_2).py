gregorian_adoption_years ={
                          'Italy': 1582,
                          'Spain': 1582,
                          'France': 1582,
                          'Portugal': 1582,
                          'Poland': 1582,
                          'Germany': 1700,
                          'United Kingdom': 1752,
                          'Sweden': 1753,
                          'Russia': 1918,
                          'Greece': 1923,
}

def gregorian_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0) 

def julian_leap_year(year):
    return year % 4 == 0

def is_leap_year(country, year):
    if year < 0:
        return 'Error: Year must be greater than 0.'
    return (gregorian_leap_year(year) if year >= gregorian_adoption_years[country] 
            else julian_leap_year(year))

# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)