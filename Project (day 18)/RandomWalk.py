import turtle
from turtle import Turtle
import random

angle = 360
tim = Turtle()
tim.pensize(5)
tim.shape("triangle")
tim.speed("fastest")
turtle.colormode(255)


def rand_color():
    r = int(random.random() * 255)
    g = int(random.random() * 255)
    b = int(random.random() * 255)
    color = (r, g, b)
    return color


def choose_way():
    global angle
    way = int(random.random() * angle)
    return way


for i in range(0, 360):
    tim.color(rand_color())
    tim.forward(15)
    tim.right(choose_way())
