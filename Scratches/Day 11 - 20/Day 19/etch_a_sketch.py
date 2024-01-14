from turtle import Turtle, Screen

tim = Turtle()
s = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


s.listen()

s.onkey(move_forward, "w")
s.onkey(move_backward, "s")
s.onkey(turn_left, "a")
s.onkey(turn_right, "d")
s.onkey(clear, "c")

s.exitonclick()
