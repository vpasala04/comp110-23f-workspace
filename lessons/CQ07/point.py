"""Defining the Point Class."""

from __future__ import annotations


class Point:
    """Representation of a point on an (x,y) coordinate graph."""

    # attributes
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Assigns initial values for the attributes x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Mutates a point by scaling/multiplying the x and y attributes by a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a new point with scaled x and y attributes."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point