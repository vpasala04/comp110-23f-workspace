"""Dictionary functions."""

__author__ = "730616700"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        if key == inverted_dict[key]:
            raise KeyError("Duplicate key in inverted_dict")
        else:
            inverted_dict[input_dict[key]] = key

print(invert({'apple': 'cat'}))

def favorite_colors(colors_dict: [str, str]) -> str:
    color_count: dict = {}
    for key, value in colors_dict.items():
        if colors_dict[item] == colors_dict[item + 1]:
            color = color + dict1[item]
            item = item + 1