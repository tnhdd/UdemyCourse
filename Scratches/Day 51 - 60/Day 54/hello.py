from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello World!</h1>"
            "<p>This is a paragraph test</p>"
            "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExazZ3NzBoNWQzbTlvdGNwcWhsbDFubHA3a3RkM3p0amdmeG14YmdwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tqj4m9BRURayxQAIW9/giphy.gif' width=300>")


@app.route("/bold")
def bold():
    return "Bold"


@app.route("/bye")
def say_bye():
    return "<p> Bye </p>"


if __name__ == "__main__":
    app.run(debug=True)
