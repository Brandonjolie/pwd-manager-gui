from tkinter import *
from tkinter import messagebox
import random, pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    name = username_input.get()
    pwd = password_input.get()
    webs = website_input.get()

    if len(pwd) == 0 or len(name) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fiels empty")
        return

    verified = messagebox.askokcancel(
        title=webs,
        message=f"These are the details entered:\nUsername:{name}\nPassword:{pwd}\nIs it ok to save?",
    )

    if verified:
        password_file = "./pwd.txt"
        with open(password_file, "a") as open_file:
            open_file.write(f"{webs} | {name} | {pwd}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "test@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(
    file="//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 29/logo.png"
)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

window.mainloop()
