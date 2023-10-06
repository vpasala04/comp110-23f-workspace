"""EX04 - 'List' Utility Functions."""

__author__ = "730616700"


def all(ints_list: list[int], value: int) -> bool:
    """Check if the integers in a given list match a given integer value."""
    list_idx: int = 0
    if len(ints_list) == 0:
        # exits loop if list is empty
        return False
    while list_idx < len(ints_list):
        if ints_list[list_idx] != value:
            return False
        list_idx += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest integer in a given list."""
    max_value: int = input[0]
    list_idx: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while list_idx < len(input):
        if input[list_idx] > max_value:
            max_value = input[list_idx]
        list_idx += 1
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determine if two intger lists have matching elements at each index."""
    list_idx: int = 0
    result: bool = True
    if len(list1) != len(list2):
        # exists loop if the length of both given lists is not the same
        return False
    while (list_idx < len(list1)):
        if list1[list_idx] != list2[list_idx]:
            result = False
        list_idx += 1
    return result