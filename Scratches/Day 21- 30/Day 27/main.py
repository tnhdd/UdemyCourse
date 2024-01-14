from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))


# Button
def button_clicked():
    # my_label["text"] = "Button clicked"
    # my_label.config(text="Button clicked")
    # print(user_input.get())
    my_label.config(text=user_input.get())


button = Button(text="Click me", command=button_clicked)

new_button = Button(text="New Button")


# Entry
user_input = Entry()

window.mainloop()
