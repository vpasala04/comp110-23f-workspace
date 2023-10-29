"""Pacman Game Scene"""

__author__ = "730616700"

from turtle import Turtle, colormode, done
colormode(255)

def main() -> None:
    """The entrypoint of my scene."""
    sun: Turtle = Turtle()
    sun.color("orange", "yellow")
    sun.begin_fill()
    sun.shape("circle")
    sun.end_fill()
    done()

if __name__ == "__main__":
    main()