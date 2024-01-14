from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __int__(self):

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=1, row=1, columnspan=2, rowspan=2)

        self.window.mainloop()
