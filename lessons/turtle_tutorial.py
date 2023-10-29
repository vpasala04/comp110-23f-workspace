from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-100, -100)
leo.pendown()

colormode(255)
leo.color("green","yellow")

leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.penup()
bob.goto(-150, -99)
bob.pendown()
i: int = 0
while i < 3:
    bob.forward(350)
    bob.left(120)
    i = i + 1

done()
