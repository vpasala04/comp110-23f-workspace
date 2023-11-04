"""Test my zip function."""

__author__ = "730616700"

from lessons.zip import zip


def test_use_case_1() -> None:
    """Test that zip returns a dictionary with a length equal to the number of keys."""
    keys: list[str] = ["Happy", "Tuesday"]
    values: list[int] = [1, 2]
    assert len(zip(keys, values)) == 2


def test_use_case_2() -> None:
    """Test that zip returns an empty dictionary when the lengths of keys and values are different."""
    keys: list[str] = ["Hi", "Happy", "Tuesday"]
    values: list[int] = [1, 2]
    assert zip(keys, values) == {}


def test_edge_case() -> None:
    """Test that an empty values list returns an empty dictionary."""
    keys: list[str] = ["Happy", "Tuesday"]
    values: list[int] = []
    assert zip(keys, values) == {}