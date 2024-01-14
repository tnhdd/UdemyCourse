import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_graph):
    for i in range(int(360 / size_of_graph)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_graph)
        tim.pensize(1.2)


draw_spirograph(8)

t.Screen().exitonclick()