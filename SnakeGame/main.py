import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


def create_snake(size):



create_snake(3)
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)

screen.exitonclick()
