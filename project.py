"""
Author: Chuy Martinez
Commit 1: Opening Lines and Temperature Conversions - Print out
name of project and author (me). Also create function to
prompt the user for a temperature & converts temp to a specified
specific temp unit

"""
# GLOBAL CONSTANTS
UNITS = {0: 'Celsius',
         1: 'Fahrenheit',
         2: 'Kelvin'}

# libary imports
import sys


def print_header():
    """Will print the project name and author name for first run"""
    print('Cisco Building 19 Temperatures ')
    print('Author: Chuy Martinez\n')


def convert_units(celsius_value, units):
    """Convert temperature to the specified units."""
    valid, celsius_value, units = validate_convert_units(celsius_value, units)
    if not valid:
        return None
    if units == 0:
        temperature = celsius_value
    if units == 1:
        temperature = (celsius_value * 9 / 5) + 32
    if units == 2:
        temperature = (celsius_value + 273.15)
    return temperature


def validate_convert_units(celsius_value, units):
    """Function that validates the data given by user being passed into convert_units"""
    valid_units = [0,1,2]
    try:
        units = int(units)
        celsius_value = float(celsius_value)
    except ValueError:
        return False, None, None
    if units not in [0,1,2]:
        return False, None, None
    return True, celsius_value, units
    

def main():
    """Orchestrate flow of our program"""
    print_header()
    celsius_value = input("Enter a temp in Celsius: ")
    units = input('Enter the desired temp unit. \n'
                  '0 - Celsius\n'
                  '1 - Fahrenheit\n'
                  '2 - Kelvin: ')
    value = convert_units(celsius_value, units)
    if not value:
        print('*** Invalid input for celsius temp or units. Try Again ***')
        sys.exit()
    else:
        units = int(units)
        print(f"{UNITS[units]} Temperature: {value}")


if __name__ == '__main__':
    main()
