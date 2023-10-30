"""Summing the elements of a list using different loops."""

__author__ = "730616700"

def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx = idx + 1
    return sum   

print(w_sum([1.1, 0.9, 1.0]))

def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for item in vals:
        sum = item + sum
    return sum

print(f_sum([1.1, 0.9, 1.0]))

def f_range_sum(vals: list[float]):
    sum: float = 0.0
    for item in range(0, len(vals)):
        sum = item + sum
    return sum

print(f_range_sum([1.1, 0.9, 1.0]))