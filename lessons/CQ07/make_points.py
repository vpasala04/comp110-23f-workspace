"""Instantiating The Point Class."""

from lessons.CQ07.point import Point

my_point: Point = Point(2.0, 3.0)

my_point.scale_by(2.0)
print("x value: ")
print(my_point.x)
print("y value: ")
print(my_point.y)

scaled_point = my_point.scale(5.0)
print("Scaled x value in new point: ")
print(scaled_point.x)
print("Scaled y value in new point:")
print(scaled_point.y)