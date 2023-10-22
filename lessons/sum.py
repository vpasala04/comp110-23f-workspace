"""Summing the elements of a list of a list using different loops."""
__author__ = "730616700"


def w_sum(vals: list[float]) -> float:
    """Calculating the sum of all elements in a list using a while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx = idx + 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculates the sum of all elements in a list using a for... in... loop."""
    sum: float = 0.0
    for number in vals:
        sum = sum + number
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculates the sum of all elements in a list using a for... in range(...) loop."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        number: float = vals[idx]
        sum = sum + number
    return sum