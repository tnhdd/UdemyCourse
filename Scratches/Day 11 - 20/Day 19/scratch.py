import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
new_turtle = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=-100 + i * 40)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You won")
            else:
                print("You lost")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
