import turtle
import random

RADIUS = 100
ANGLE = 360

tim = turtle.Turtle()
tim.shape("triangle")
tim.speed("fastest")

turtle.colormode(255)


def rand_color():
    r = int(random.random() * 255)
    g = int(random.random() * 255)
    b = int(random.random() * 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(rand_color())
        tim.circle(RADIUS)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(40)

screen = turtle.Screen()
screen.exitonclick()