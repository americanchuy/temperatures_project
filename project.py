"""
Author: Chuy Martinez
Commit 1: Opening Lines and Temperature Conversions - Print out
name of project and author (me). Also create function to
prompt the user for a temperature & converts temp to a specified
specific temp unit

Commit 2: Implementing a menu for users. This provides the interface for the user to interact with the program

"""
# GLOBAL CONSTANTS
UNITS = {0: 'Celsius',
         1: 'Fahrenheit',
         2: 'Kelvin'}

# library imports
import sys


def print_header():
    """Will print the project name and author name for first run"""
    print('Cisco Building 19 Temperatures ')
    print('Author: Chuy Martinez')


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
    valid_units = [0, 1, 2]
    try:
        units = int(units)
        celsius_value = float(celsius_value)
    except ValueError:
        return False, None, None
    if units not in [0, 1, 2]:
        return False, None, None
    return True, celsius_value, units


def print_menu():
    """Creating  a menu that will be rendered to our users to enable user interaction"""
    print("Main Menu\n---------\n"
          "1 - Process a new data file\n"
          "2 - Choose Units\n"
          "3 - Edit room filter\n"
          "4 - Show summary statistics\n"
          "5 - Show temperature by date and time\n"
          "6 - Show histogram of temperatures\n"
          "7 - Quit")


def new_file(dataset):
    """Stub function for now"""
    print('New File Function Called')


def choose_units():
    """Stub function for now"""
    print('Choose Units Function Called')


def change_filter(sensor_list, active_sensors):
    """Stub function for now"""
    print('Change Filter Function Called')


def print_summary_statistics(dataset, active_sensors):
    """Stub function for now"""
    print('Summary Statistics Function Called')


def print_temp_by_day_time(dataset, active_sensors):
    """Stub function for now"""
    print('Print Temp By Day/Time Function Called')


def print_histogram(dataset, active_sensors):
    """Stub function for now"""
    print('Print Histogram Function Called')


def function_caller(choice, dataset=None, active_sensors=None, sensor_list=None):
    if choice == 1:
        new_file(dataset)
    if choice == 2:
        choose_units()
    if choice == 3:
        change_filter(sensor_list, active_sensors)
    if choice == 4:
        print_summary_statistics(dataset, active_sensors)
    if choice == 5:
        print_temp_by_day_time(dataset, active_sensors)
    if choice == 6:
        print_histogram(dataset, active_sensors)
    if choice == 7:
        print('Thanks for using Cisco Building 19 Temp project. Goodbye!')
        sys.exit()
    print()


def main():
    """Orchestrate flow of our program"""
    print_header()
    menu_options = [num for num in range(1, 8)]
    while True:
        print_menu()
        print()
        choice = input('What is your choice? ')
        try:
            choice = int(choice)
        except ValueError:
            print("*** Please enter a number only ***")
            continue
        if choice not in menu_options:
            print('*** Please enter a number between 1 and 7 ***')
            continue
        function_caller(choice)


if __name__ == '__main__':
    main()
