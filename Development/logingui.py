from tkinter import *
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import ImageTk, Image

root = tb.Window(themename="superhero")
root.title("Login")
root.geometry("600x600")

def login():
    username = "admin"
    password = "1"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Successful", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")


username_entry = tb.Entry(root, font=("Arial", 16))
username_entry.insert(0, "Username")
password_entry = tb.Entry(root, show="*", font=("Arial", 16))
password_entry.insert(0, "Password")
login_button = tb.Button(root, text="Login", command=login, width=4)
createacc_button = tb.Button(root, text="Create Account", width=11)

username_entry.place(x=200, y=300)
password_entry.place(x=200, y=350)
login_button.place(x=200, y=400)
createacc_button.place(x=270, y=400)

root.mainloop()
