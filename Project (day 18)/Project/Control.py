from turtle import Turtle, Screen

tim = Turtle()
tim.shape("triangle")
screen = Screen()


def move():
    tim.forward(20)


def left():
    tim.setheading(tim.heading() + 10)


def right():
    tim.setheading(tim.heading() - 10)


def back():
    tim.forward(-20)


def clear():
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
