import random
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    p_letters = [choice(letters) for i in range(randint(8, 10))]
    p_numbers = [choice(numbers) for i in range(randint(2, 4))]
    p_symbols = [choice(symbols) for i in range(randint(2, 4))]

    password_list = p_symbols + p_numbers + p_letters
    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please dont let any field empty")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered\n Email: {email}\n Password: {password}")

        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.writelines(f"{website} | {email} | {password}\n")
                input_password.delete(0, END)
                input_website.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Input texts
input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "tuan@email.com")
input_password = Entry(width=20)
input_password.grid(row=3, column=1)

# Buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=35, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
