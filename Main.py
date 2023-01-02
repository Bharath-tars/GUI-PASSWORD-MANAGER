from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers+password_letters+password_symbols
    random.shuffle(password_list)

    shuf_pass = "".join(password_list)
    e3.insert(0, string=shuf_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    if len(e1.get()) == 0 or len(e2.get()) ==0:
        messagebox.showinfo(title="ERROR", message="Please the enter the details!.. U've left them empty")
    else:
        is_ok = messagebox.askyesno(title="Confirmation",message=f"Are the Entered Details\nName:{e1.get()}\nPassword:{e3.get()}\nTrue?")
        if is_ok:
            with open("data.txt", "a") as add_data:
                add_data.write(f"{e1.get()} | {e2.get()} | {e3.get()}\n")
                print("done uploading")
        e1.delete(0, END)
        e3.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


l1 = Label(text="Website:")
l1.grid(row=1, column=0)

e1 = Entry(width=35)
e1.grid(row=1, column=1, columnspan=2)
e1.focus()

l2 = Label(text="Email/Username:")
l2.grid(row=2, column=0)

e2 = Entry(width=35)
e2.insert(0, "yo@gmail.com")
e2.grid(row=2, column=1, columnspan=2)

l3 = Label(text="Password:")
l3.grid(row=3, column=0)

e3 = Entry(width=21)
e3.grid(row=3, column=1)

b = Button(text="Add", width=36, command=save_data)
b.grid(row=4, column=1)

b1 = Button(text="Generate Password", command=generate_pass)
b1.grid(row=3, column=2)
window.mainloop()
