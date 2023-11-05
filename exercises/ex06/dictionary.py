"""Dictionary functions."""

__author__ = "730616700"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dict."""
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        if input_dict[key] in inverted_dict:
            raise KeyError("Duplicate key in inverted_dict")
        inverted_dict[input_dict[key]] = key
    return inverted_dict


def favorite_color(colors_dict: dict[str, str]) -> str:
    """Returns which color appears most frequently."""
    color_count: dict[str, int] = {}
    max_count: int = 0
    final_color: str = ""
    for key in colors_dict:
        color = colors_dict[key]
        if color in color_count:
            color_count[color] = color_count[color] + 1
        else:
            color_count[color] = 1
    for color in color_count:
        if color_count[color] > max_count:
            max_count = color_count[color]
            final_color = color
        elif final_color == "":
            final_color = colors_dict[key]
    return final_color


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dictionary mapping list values to their frequency counts."""
    final_dict: dict[str, int] = {}
    for key in input_list:
        if key in final_dict:
            final_dict[key] = final_dict[key] + 1
        else:
            final_dict[key] = 1
    return final_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary with unique alphabet letters as keys and lists of words that start with each letter as values."""
    final_dict: dict[str, list[str]] = {}
    for word in input_list:
        first_letter = word[0].lower()
        if first_letter in final_dict:
            final_dict[first_letter].append(word)
        else:
            final_dict[first_letter] = [word]
    return final_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates and returns a dictionary with attendance information for a given day of the week and student."""
    if day in attendance_dict:
        attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict