from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)

user_input = Entry()
user_input.grid(row=0, column=1)

txt_miles = Label(text="Miles")
txt_miles.grid(row=0, column=2)

lbl_equals = Label(text="is equals to")
lbl_equals.grid(row=1, column=0)

lbl_result = Label(text="")
lbl_result.grid(row=1, column=1)

lbl_km = Label(text="Km")
lbl_km.grid(row=1, column=2)


def converter():
    result = (float(user_input.get()) * 1.609344)
    lbl_result.config(text=result)


btt_Calculate = Button(text="Calculate", command=converter)
btt_Calculate.grid(row=2, column=1)

window.mainloop()
