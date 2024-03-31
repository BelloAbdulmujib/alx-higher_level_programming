#!/usr/bin/python3
"""Finds a peak in an unsorted list of integers.

    Args:
        list_of_integers (list[int]): The input list of integers.

    Returns:
        int: The peak value found in the list.

    Complexity:
        The complexity of this algorithm is O(log(n)).

    Note:
        There may be more than one peak in the list
"""


def find_peak(list_of_integers):

    if not list_of_integers:
        return None

        left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:

            left = mid + 1
        else:

            right = mid

    return list_of_integers[left]


my_list = [1, 3, 5, 9, 7, 4, 2]
peak_value = find_peak(my_list)
print(f"The peak value in the list is: {peak_value}")
