from turtle import 

class Snake:
    snake = []
    snake_positions = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        for pos in snake_positions:
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            snake.append(segment)