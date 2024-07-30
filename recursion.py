"""
Author: Chuy Martinez
Purpose: Using recursion to reverse a list
Recursion reqs:
    1. Everytime the function is recursively called, the new input must be a smaller list
    2. Each recursive call must get us closer to the base case
    3. Once the base case is reached, this is when recursion ends
"""

from string import ascii_lowercase as letters


def reverse_a_list(lst):
    length = len(lst)
    print(f"The length of my_list is now: {length}")
    if length <= 1:
        return lst
    else:
        last_letter = lst[-1]
        new_list = lst[:-1]
        return [last_letter] + reverse_a_list(new_list)


def main():
    """
    Unit test - make sure that the original list is not modified after reverse_a_list is called
    """
    alphabet = [letter for letter in letters]
    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()
