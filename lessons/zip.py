"""Combining two lists into a dictionary."""

__author__ = "730616700"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    """Creating a dictionary by pairing the elements from two lists."""
    full_dict: dict[str, int] = {}
    idx: int = 0
    if len(keys) != len(values) or len(keys) + len(values) == 0:
        full_dict = {}
        return full_dict
    for item in keys:
        dict[item] = values[idx]
        idx = idx + 1
    return full_dict