from turtle import Turtle
import random

shapes = [
    {"triangle": 3},
    {"square": 4},
    {"pentagon": 5},
    {"hexagon": 6},
    {"heptagon": 7},
    {"octagon": 8},
    {"nonagon": 9}, 
    {"decagon": 10},
]

tim = Turtle()
tim.shape("triangle")


def draw_shape(num_sides):
    for sides in num_sides:
        angle = 360 / sides
        for side in range(0, sides):
            tim.forward(100)
            tim.right(angle)


for shape in shapes:
    draw_shape(shape.values())
