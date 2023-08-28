from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import os
from PIL import ImageTk,Image

# Designing window for registration

def register():
    """
    Creates a new registration screen and initializes the necessary global variables.
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
    """
    Opens a new login screen window where the user can enter their login details.
    
    Parameters:
        None
    
    Returns:
        None
    """
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
    """
    Registers a user by writing their username and password to a file.
    
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
    tb.Label(register_screen, text="Registration Success", font=("calibri", 11)).place(x=1, y=1)

# Implementing event on login button 

def login_verify():
    """
    Function to verify login credentials.
    
    This function takes no parameters.
    
    It retrieves the username and password entered by the user from two different entry fields.
    It then clears the contents of both entry fields.
    
    It retrieves a list of files in the current directory using the `os.listdir()` function.
    If the entered username is found in the list of files, it opens the corresponding file in read mode.
    It reads the contents of the file and splits them into a list of lines.
    
    If the entered password is found in the list of lines, it calls the `login_success()` function.
    Otherwise, it calls the `password_not_recognized()` function.
    
    If the entered username is not found in the list of files, it calls the `user_not_found()` function.
    
    This function does not return any values.
    """
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
    """
    Creates a new window to display a success message after a successful login.

    This function does not take any parameters.

    Returns:
        None
    """
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    tb.Label(login_success_screen, text="Login Success").place(x=1, y=1)
    tb.Button(login_success_screen, text="OK", command=main_gui).place(x=20, y=20)

# Designing popup for login invalid password

def password_not_recognised():
    """
    Displays a screen indicating that the password entered was not recognised.

    Parameters:
        None

    Returns:
        None
    """
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    tb.Label(password_not_recog_screen, text="Invalid Password ").place(x=1, y=1)
    tb.Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).place(x=20, y=20)

# Designing popup for user not found

def user_not_found():
    """
    Create a new window to display a "User Not Found" message.

    This function creates a new window using the Toplevel class from the tkinter library. 
    The window is titled "Success" and has dimensions of 150x100 pixels. 
    It displays a label with the text "User Not Found" at coordinates (1,1) and a button with the text "OK" at coordinates (20,20). 
    Clicking the button will call the `delete_user_not_found_screen` function.

    Parameters:
        None

    Returns:
        None
    """
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    tb.Label(user_not_found_screen, text="User Not Found").place(x=1, y=1)
    tb.Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).place(x=20, y=20)

# Deleting popups

def delete_password_not_recognised():
    """
    Deletes the password_not_recog_screen.

    This function destroys the password_not_recog_screen widget, removing it from the GUI.

    Parameters:
        None

    Returns:
        None
    """
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    """
    Delete the user not found screen.

    This function destroys the user not found screen.

    Parameters:
        None

    Returns:
        None
    """
    user_not_found_screen.destroy()

def main_gui():
    """
    Creates and displays the main graphical user interface (GUI) of the application.
    This function destroys any existing login screens or windows and creates a new window
    with a specified theme, size, and title. It also loads and displays an image on the window.
    
    Parameters:
        None

    Returns:
        None
    """
    login_success_screen.destroy()
    login_screen.destroy()
    root.destroy()

    main_gui = tb.Window(themename="superhero")
    main_gui.geometry("2560x1600")
    main_gui.title("Exercise Planner")

    image = Image.open("image.png")
    resized_image = image.resize((400, 500))
    tk_image = ImageTk.PhotoImage(resized_image)
    label = Label(main_gui, image=tk_image)
    label.place(x=1, y=1)


    columns = ("Exercise", "Sets", "Reps")
    tree = tb.Treeview(main_gui, columns=columns, show="headings", height=10)
    tree.place(x=430, y=30)

    tree.heading("Exercise", text="Exercise")
    tree.heading("Sets", text="Sets")
    tree.heading("Reps", text="Reps")

    def triceps_add():
        tree.delete(*tree.get_children())  

        items_to_add = [
            ("Press Down", "3", "10"),
            ("Shoulder Press", "4", "10"),
            ("Closed Grip Bench Press", "2", "8")
        ]

        for item in items_to_add:
            tree.insert("", "end", values=item)

    def biceps_add():
        tree.delete(*tree.get_children())  

        items_to_add = [
            ("Hammer Curl", "3", "10"),
            ("Incline Bicep Curl", "3", "12"),
            ("Barbell Curl", "3", "8")
        ]

        for item in items_to_add:
            tree.insert("", "end", values=item)

    def legs_add():
        tree.delete(*tree.get_children())  

        items_to_add = [
            ("Back Squats", "3", "10"),
            ("Calf Raises", "3", "15"),
            ("Hip Thrusts", "3", "8")
        ]

        for item in items_to_add:
            tree.insert("", "end", values=item)

    def back_add():
        tree.delete(*tree.get_children())  

        items_to_add = [
            ("Lat pulldown", "3", "10"),
            ("Deadlift", "3", "6"),
            ("Barbell Row", "3", "8")
        ]

        for item in items_to_add:
            tree.insert("", "end", values=item)

    def abs_add():
        tree.delete(*tree.get_children())  

        items_to_add = [
            ("Knee to Elbow Crunch", "3", "10"),
            ("Sit Ups", "3", "10"),
            ("Elbow Plank", "3", "10")
        ]

        for item in items_to_add:
            tree.insert("", "end", values=item)

    def chest_add():
        tree.delete(*tree.get_children())  

        items_to_add = [
            ("Bench Press", "3", "10"),
            ("Inclined Press", "3", "10"),
            ("Chest Dips", "2", "8")
        ]

        for item in items_to_add:
            tree.insert("", "end", values=item)

    def shoulders_add():
        tree.delete(*tree.get_children())  

        items_to_add = [
            ("Shoulder Press", "3", "10"),
            ("Seated Raises", "3", "10"),
            ("Lateral Raise", "3", "10")
        ]

        for item in items_to_add:
            tree.insert("", "end", values=item)


    triceps = tb.Button(bootstyle="success", text="Triceps", command=triceps_add)
    triceps.place(x=0, y=550)
    biceps = tb.Button(bootstyle="success", text="Biceps", command=biceps_add)
    biceps.place(x=100, y=550)
    legs = tb.Button(bootstyle="success", text="Legs", command=legs_add)
    legs.place(x=200, y=550)
    back = tb.Button(bootstyle="success", text="Back", command=back_add)
    back.place(x=300, y=550)
    abs = tb.Button(bootstyle="success", text="Abs", command=abs_add)
    abs.place(x=400, y=550)
    chest = tb.Button(bootstyle="success", text="Chest", command=chest_add)
    chest.place(x=500, y=550)
    shoulders = tb.Button(bootstyle="success", text="Shoulders", command=shoulders_add)
    shoulders.place(x=600, y=550)



    tree2 = tb.Treeview(main_gui, columns=columns, show="headings", height=10)
    tree2.place(x=430, y=30)

    tree2.heading("Exercise", text="Exercise")
    tree2.heading("Sets", text="Sets")
    tree2.heading("Reps", text="Reps")


    main_gui.mainloop()








root = tb.Window(themename="superhero")
root.geometry("300x250")
root.title("Account Login")
tb.Label(text="Select Your Choice").place(x=85, y=30)
tb.Button(text="Login", command=login).place(x=80, y=60)
tb.Button(text="Register", command=register).place(x=140, y=60)

root.mainloop()