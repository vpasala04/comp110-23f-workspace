"""Combining two lists into a dictionary."""

__author__ = "730616700"
    

def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    idx: int = 0
    new_dict: dict = {}
    if len(list1) != len(list2) or len(list1) == 0 or len(list2) == 0:
        return new_dict
    for item in list1:
        new_dict[item] = list2[idx]
        idx = idx + 1
    return new_dict

print(zip(["Happy", "Tuesday"],[1,2]))