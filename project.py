"""
Author: Chuy Martinez
Commit 1: Opening Lines and Temperature Conversions - Print out
name of project and author (me). Also create function to
prompt the user for a temperature & converts temp to a specified
specific temp unit

Commit 2: Implementing a menu for users. This provides the interface for the user to interact with the program

Commit 3: Creating containers that hold our data. Each container will include 3 pieces of information. 1) the sensor number,
2) the room number where sensor is located, 3) the room description, the name of the room
"""

# library imports
import sys

# GLOBAL CONSTANTS
UNITS = {0: 'Celsius',
         1: 'Fahrenheit',
         2: 'Kelvin'}


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
        print('Thanks for using the Cisco Campus Temperature Project. Goodbye!')
        sys.exit()
    print()


def main():
    """Main for this commit is designed to create the data structures for this program and serves as a unit test."""
    print_header()
    # key - room number
    # value - (sensor number, room description/name)
    sensors = {
        '4213': ('Cisco Building 19', 0),
        '4201': ('Cisco Building 21', 1),
        '4204': ('Cisco Building 13 Cafeteria', 2),
        '4218': ('Hardware Room', 3),
        '4205': ('Software Room', 4),
        'Out': ('Out', 5)
    }
    # use a list comprehension to turn each key value pair from the dict into a list of tuples.
    sensor_list = [(key, *value) for (key,value) in sensors.items()]
    # this will contain a filtered list of currently active sensors
    filter_list = [value[1] for (key,value) in sensors.items()]
    print('Testing sensors: ')
    if sensors['4213'][0] == 'Cisco Building 19' and sensors['Out'][1] == 5:
        print('Pass')
    else:
        print('Fail')
    print('Testing sensor_list length: ')
    if len(sensor_list) == 6:
        print('Pass')
        print('Testing sensor_list content: ')
        for item in sensor_list:
            if item[1] != sensors[item[0]][0]:
                print('Fail')
                break
        else:
            print('Pass')
    print('Testing filter_list length: ')
    if len(filter_list) == 6:
        print('Pass')
    else:
        print('Fail')
    print('Testing filter_list content:')
    if sum(filter_list) == 15:
        print('Pass')
    else:
        print('Fail')

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
