"""EX04 - 'List' Utility Functions."""

__author__ = "730616700"

def all(ints_list: list[int], value: int) -> bool:
    list_idx: int = 0
    result: bool = False
    if len(ints_list) == 0:
        return result
    while list_idx < len(ints_list):
        if ints_list[list_idx] == value:
            result = True
        else:
            result = False
        list_idx += 1
    return result

def max(input: list[int]) -> int:
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
    list1_idx: int = 0
    list2_idx: int = 0
    result: bool = False
    while (list1_idx < len(list1)):
        if list1[list1_idx] == list2[list2_idx]:
            result = True
        else:
            result = False
        list1_idx += 1
    return result

print(is_equal([1, 0, 1], [1, 0, 1]))
print(is_equal([1, 1, 0], [1, 0, 1]))
print(is_equal([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]))