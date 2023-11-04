"""Dictionary functions."""

__author__ = "730616700"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a list."""
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in inverted_dict:
            raise KeyError("Duplicate key in inverted_dict")
        inverted_dict[input_dict[key]] = key
    return inverted_dict

print(invert({'apple': 'cat'}))

def favorite_color(colors_dict: [str, str]) -> str:
    """Returns which color appears most frequently."""
    color_count: dict[str, int] = {}
    max_count: int = 0
    final_color: str = ""
    for key in colors_dict:
        if key in color_count:
            color_count = color_count + 1
        else:
            color_count = 1
    for key in color_count:
        if color_count[key] > max_count:
            max_count = color_count[key]
            final_color = key
    return final_color

print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))
        


