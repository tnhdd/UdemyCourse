from turtle import Turtle

FONT = ("Courier", 14, "normal")


class WriteName(Turtle):
    def __init__(self, name, x_cor, y_cor):
        super().__init__()
        self.write(name, font=FONT)
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
