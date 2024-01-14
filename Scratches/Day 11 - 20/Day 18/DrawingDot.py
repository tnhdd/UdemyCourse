import random
import turtle as t

t.colormode(255)
tim = t.Turtle

color_list = [(202, 165, 109), (238, 249, 142)]


for i in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

t.Screen().exitonclick()
