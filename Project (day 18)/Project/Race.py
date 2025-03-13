from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ("red", "green", "blue", "yellow", "light sky blue", "pink")
turtles = []

y_pos = (-150, -90, -30, 30, 90, 150)


def compare_bet(bet, color):
    if bet == color:
        print(f"You won the game the {color} turtle is first")
    else:
        print(f"You lose! The {color} turtle is first")


def place_turtle(turtle, y):
    turtle.penup()
    turtle.goto(x=-230, y=y)


is_race = True
for i in range(0, 6):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(colors[i])
    turtles.append(tim)
    place_turtle(tim, y_pos[i])
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    while is_race:
        for turtle in turtles:
            if turtle.xcor() > 235:
                is_race = False
                compare_bet(user_bet, turtle.pencolor())
            else:
                rand = random.randint(0, 10)
                turtle.forward(rand)


screen.exitonclick()
