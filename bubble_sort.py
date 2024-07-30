"""
Author: Chuy Martinez
Bubble sort using recursion
Note: Recursion is expensive in terms of both memory and processing time.
Program spec:
    - add function recursive_sort() which has as its parameters, list_to_sort(a list of tuples), and a key
    - key should have a default value of 0 and refers to whether the list should be sorted by the
        first or second value in the tuple
    - recursive_sort() should call itself as part of the process
    - when exchanging the items in the list, use tuple unpacking
    - the sorted part of the list will be growing from the end of the list (the greatest value).
    - each time recursive_sort() is called, it should take in a smaller list
    - use slicing
    - add a regular_bubble_sort() functon that also takes in list_to_sort, and key
        - use a while loop instead of recursion

"""


def recursive_sort(list_to_sort, key=0):
    length = len(list_to_sort)
    # make a copy of list so the original list is not modified
    lst = list_to_sort[:]
    if length <= 1:
        return lst
    else:
        for idx in range(length - 1):
            if lst[idx][key] > lst[idx + 1][key]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
        last_item = lst[-1]
        new_lst = lst[:-1]
        return recursive_sort(new_lst, key) + [last_item]


def regular_bubble_sort(list_to_sort, key=0):
    length = len(list_to_sort)
    # make a copy of the list so the original list is not modified
    lst = list_to_sort[:]
    while True:
        count = 0
        for idx in range(length - 1):
            if lst[idx][key] > lst[idx + 1][key]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                count += 1
        if count == 0:
            return lst


def main():
    sensor_list = [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1),
                   ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3),
                   ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]
    print("\nOriginal unsorted list\n", sensor_list)
    print("\nList sorted by room number\n", recursive_sort(sensor_list, 0))
    print("\nList sorted by room name\n", recursive_sort(sensor_list, 1))
    print("\nOriginal unsorted list\n", sensor_list)


if __name__ == "__main__":
    main()
