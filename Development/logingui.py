from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import os
from PIL import ImageTk,Image

# Designing window for registration

def register():
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
    tb.Label(register_screen, text="Please enter details below").place(x=45, y=30)
    username_label = tb.Label(register_screen, text="Username * ").place(x=40, y=60)
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.place(x=40, y=80)
    password_label = tb.Label(register_screen, text="Password * ").place(x=40, y=120)
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.place(x=40, y=140)
    tb.Button(register_screen, text="Register", command = register_user).place(x=110, y=190)

# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    tb.Label(login_screen, text="Please enter details below to login").place(x=45, y=30)
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    tb.Label(login_screen, text="Username * ").place(x=40, y=60)
    username_login_entry = tb.Entry(login_screen, textvariable=username_verify)
    username_login_entry.place(x=40, y=80)
    tb.Label(login_screen, text="Password * ").place(x=40, y=120)
    password_login_entry = tb.Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.place(x=40, y=140)
    tb.Button(login_screen, text="Login", command = login_verify).place(x=110, y=190)

# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    tb.Label(register_screen, text="Registration Success", font=("calibri", 11)).place(x=1, y=1)

# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

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

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    tb.Label(login_success_screen, text="Login Success").place(x=1, y=1)
    tb.Button(login_success_screen, text="OK", command=main_gui).place(x=20, y=20)

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    tb.Label(password_not_recog_screen, text="Invalid Password ").place(x=1, y=1)
    tb.Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).place(x=20, y=20)

# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    tb.Label(user_not_found_screen, text="User Not Found").place(x=1, y=1)
    tb.Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).place(x=20, y=20)

# Deleting popups

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_gui():
    login_success_screen.destroy()
    login_screen.destroy()
    root.destroy()

    main_gui = tb.Window(themename="superhero")
    main_gui.geometry("500x500")
    main_gui.title("Exercise Planner")

    canvas = Canvas(main_gui)
    canvas.place(x=10, y=10)
    img = ImageTk.PhotoImage(Image.open("image.png"))
    canvas.create_image(1,1,anchor=NW,image=img)



    main_gui.mainloop()








root = tb.Window(themename="superhero")
root.geometry("300x250")
root.title("Account Login")
tb.Label(text="Select Your Choice").place(x=85, y=30)
tb.Button(text="Login", command=login).place(x=80, y=60)
tb.Button(text="Register", command=register).place(x=140, y=60)

root.mainloop()