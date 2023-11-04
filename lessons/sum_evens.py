"""Practice summing over lists."""

def sum_evens_in_list(input_list: list[int]) -> int:
    """Sums all the even numbers in a list together."""
    total_sum: int = 0
    for num in input_list:
        if num % 2 == 0:
            total_sum = total_sum + num
    return total_sum
            