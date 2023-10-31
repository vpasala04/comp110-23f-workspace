
def odd_and_even(input: list[int]) -> list[int]:
    idx: int = 0
    new_list: list[int] = []
    for elem in input:
        if idx % 2 == 0 and input[idx] % 2 != 0 and idx < len(input):
            new_list = new_list + input[idx]
        idx = idx + 1
    return new_list
