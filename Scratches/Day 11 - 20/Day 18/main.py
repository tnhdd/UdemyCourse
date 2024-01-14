import random
from random import randrange
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed(0)
for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

tim.done
