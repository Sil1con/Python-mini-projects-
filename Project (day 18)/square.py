from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

# for i in range(0, 4):
#     tim.forward(100)
#     tim.right(90)

for i in range(1, 50):
    if i % 2 == 0:
        tim.forward(5)
        tim.pencolor("black")
    elif i % 2 != 0:
        tim.forward(5)
        tim.pencolor("white")



screen = Screen()
screen.exitonclick()
