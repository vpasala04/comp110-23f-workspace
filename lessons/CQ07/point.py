"""Defining the Point Class."""

from __future__ import annotations


class Point:
    """Representation of a point on an (x,y) coordinate graph."""

    # attributes
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
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
    
    def __str__(self) -> str:
        """Returns a readable representation of a Point object."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: (int | float)) -> Point:
        """Multiply the x and y attributes of the Point by a factor."""
        new_x: int = self.x * factor
        new_y: int = self.y * factor
        return Point(new_x, new_y)

    def __add__(self, value: (int | float)) -> Point:
        """Add a value to the x and y attributes to create a new Point."""
        new_x: int = self.x + value
        new_y: int = self.y + value
        return Point(new_x, new_y)