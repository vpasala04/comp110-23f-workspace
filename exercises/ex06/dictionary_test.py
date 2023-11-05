"""Dictionary Unit Tests."""


__author__ = "730616700"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
import pytest


def test_key_error() -> None:
    """Test that the function raises KeyError when value from input dict is a key in inverted dict."""
    with pytest.raises(KeyError):
        my_dict = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dict)


def test_empty_dict() -> None:
    """Test function with empty dictionary."""
    test_dict: dict = {}
    assert invert(test_dict) == {}


def test_dict_len() -> None:
    """Test function with an input dict length of 1."""
    test_dict: dict = {"Happy": "Birthday"}
    assert invert(test_dict) == {"Birthday": "Happy"}


def test_valid_dict() -> None:
    """Test function with a valid dictionary."""
    test_dict: dict = {"Vineeta": "red", "Lena": "blue", "Rain": "red"}
    assert favorite_color(test_dict) == "red"


def test_empty_dict() -> None:
    """Test function with an empty dictionary."""
    test_dict: dict = {}
    assert favorite_color(test_dict) == ""


def test_dict_len() -> None:
    """Test function with an input dict length of 1."""
    test_dict: dict = {"Alexa": "yellow"}
    assert favorite_color(test_dict) == "yellow"


def test_valid_list() -> None:
    """Test function with a valid list."""
    test_list: list = ["Houston", "Charlotte", "Houston", "Austin", "Raleigh", "Seattle", "Dallas", "Seattle", "Seattle"]
    assert count(test_list) == {"Houston": 2, "Charlotte": 1, "Austin": 1, "Raleigh": 1, "Seattle": 3, "Dallas": 1}


def test_list_len() -> None:
    """Test function with an input list length of 1."""
    test_list: list = ["Chocolate"]
    assert count(test_list) == {"Chocolate": 1}


def test_empty_list() -> None:
    """Test function with an empty list."""
    test_list: list = []
    assert count(test_list) == {}


def test_valid_list() -> None:
    """Test function with a valid list."""
    test_list: list = ["water", "waves", "ocean", "octopus", "tentacle"]
    assert alphabetizer(test_list) == {"w": ["water", "waves"], "o": ["ocean", "octopus"], "t": ["tentacle"]}


def test_list_len() -> None:
    """Test function with an input list length of 1."""
    test_list: list = ["peanut"]
    assert alphabetizer(test_list) == {"p": ["peanut"]}


def test_empty_list() -> None:
    """Test function with an empty list."""
    test_list: list = []
    assert alphabetizer(test_list) == {}


def test_new_student() -> None:
    """Test function with adding a new student to an existing day in input dictionary."""
    test_dict: dict = {"Monday": ["Ranger", "Param"], "Tuesday": ["Jackapoo"]}
    assert update_attendance(test_dict, "Tuesday", "Tanny") == {"Monday": ["Ranger", "Param"], "Tuesday": ["Jackapoo", "Tanny"]}


def test_new_day() -> None:
    """Test function with adding a new day and new student to a dictionary."""
    test_dict: dict = {"Monday": ["Ranger", "Param"], "Tuesday": ["Jackapoo"]}
    assert update_attendance(test_dict, "Wednesday", "Ronaldo") == {"Monday": ["Ranger", "Param"], "Tuesday": ["Jackapoo"], "Wednesday": ["Ronaldo"]}


def test_empty_dict() -> None:
    """Test function with an empty dictionary."""
    test_dict: dict = {}
    assert update_attendance(test_dict, "Thursday", "Rio") == {"Thursday": ["Rio"]}







    


