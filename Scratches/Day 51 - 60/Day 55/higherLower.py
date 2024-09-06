from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def welcome():
    return ("<h1 style='bold'>Guess a number between 0 and 9</h1>"
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXE1cnc4emR1dGVqaHIwc2Y4cmhxaGFydHdwNGt4bzRjcXZoZ2toYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378khQxt68syiWJy/giphy.webp'>")


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return ("<h1 style='color: red'>Too high, try again!</h1>"
                "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXViZWhmYmE0dWdyYXhycHN0aTF0cGR0OHMwYnZ4Mm55MXh4OGkxaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IuWMpDm2PdTL8s/giphy.webp'>")
    elif guess == random_number:
        return ("<h1 style='color: red'>That's correct</h1>"
                "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDBwNGwyanR3cG53bW5jMGIwNWV1M3lnOHU5OHJtN202N24xOTJ0NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3WCNY2RhcmnwGbKbCi/giphy.webp'>")
    else:
        return ("<h1 style='color: red'>Too low, try again!</h1>"
                "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzNwdjhpYTBwamlmM2Z0dmdoZ2s2Y3E3bDhiMzRvZnd2azd3N3QyZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.webp'>")


if __name__ == "__main__":
    app.run(debug=True)
