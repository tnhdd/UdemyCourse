import turtle

a_turtle = turtle.Turtle()
colors = ["pink", "yellow", "blue", "green", "white", "red"]
turtle.bgcolor("black")

for i in range(200):
    a_turtle.pencolor(colors[i % 6])
    a_turtle.width(i / 100 + 1)
    a_turtle.forward(i)
    a_turtle.left(59)

turtle.done()