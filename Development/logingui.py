from tkinter import *
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import os

root = tb.Window(themename="superhero")
root.title("Login")
root.geometry("600x600")

# def login():
#     """
#     Logs in a user with the provided username and password.

#     This function compares the values entered in the username and password fields
#     with the predefined values for username and password. If the values match, it
#     displays a success message box. Otherwise, it displays an error message box.

#     Parameters:
#         None

#     Returns:
#         None
#     """
#     username = "admin"
#     password = "1"
#     if username_entry.get()==username and password_entry.get()==password:
#         messagebox.showinfo(title="Login Successful", message="You successfully logged in.")
#     else:
#         messagebox.showerror(title="Error", message="Invalid login.")

def login():
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Button(root, text="Login", width=10, height=1, command =login_verify).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(root)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(root)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(root)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()

def register():
    """
    Initializes the registration process by creating a new window and setting its properties.
    
    Parameters:
        None
    
    Returns:
        None
    """
    global register_screen
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    tb.Label(register_screen, text="Please enter your new account details below").place(x=20, y=20)
    tb.Label(register_screen, text="").place(x=20, y=50)
    username_lable = tb.Label(register_screen, text="Username * ")
    username_lable.place(x=20, y=80)
    username_entry = tb.Entry(register_screen, textvariable=username)
    username_entry.place(x=20, y=110)
    password_lable = tb.Label(register_screen, text="Password * ")
    password_lable.place(x=20, y=140)
    password_entry = tb.Entry(register_screen, textvariable=password, show='*')
    password_entry.place(x=20, y=170)
    tb.Label(register_screen, text="").place()
    tb.Button(register_screen, text="Register", command = register_user).place(x=20, y=210)

def register_user():
    """
    Gets the username and password from the register screen and saves them to a file

    Parameters:
        None

    Returns:
        None
    """
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)



username_entry = tb.Entry(root, textvariable=username_verify, font=("Arial", 16))
username_entry.insert(0, "Username")
password_entry = tb.Entry(root, textvariable=password_verify, show="*", font=("Arial", 16))
password_entry.insert(0, "Password")
login_button = tb.Button(root, text="Login", command=login, width=4)
createacc_button = tb.Button(root, text="Create Account", command=register, width=11)

username_entry.place(x=200, y=300)
password_entry.place(x=200, y=350)
login_button.place(x=200, y=400)
createacc_button.place(x=270, y=400)

root.mainloop()
