from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import os
from PIL import ImageTk,Image











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
tree.place(x=410, y=30)

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
biceps.place(x=80, y=550)
legs = tb.Button(bootstyle="success", text="Legs", command=legs_add)
legs.place(x=155, y=550)
back = tb.Button(bootstyle="success", text="Back", command=back_add)
back.place(x=220, y=550)
abs = tb.Button(bootstyle="success", text="Abs", command=abs_add)
abs.place(x=285, y=550)
chest = tb.Button(bootstyle="success", text="Chest", command=chest_add)
chest.place(x=345, y=550)
shoulders = tb.Button(bootstyle="success", text="Shoulders", command=shoulders_add)
shoulders.place(x=415, y=550)

tree2 = tb.Treeview(main_gui, columns=columns, show="headings", height=10)
tree2.place(x=800, y=400)

tree2.heading("Exercise", text="Exercise")
tree2.heading("Sets", text="Sets")
tree2.heading("Reps", text="Reps")

def add_selected_item():
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")
        tree2.insert("", "end", values=values)

add_button = tb.Button(main_gui, text="Add Selected Item", command=add_selected_item)
add_button.place(x=630, y=250)


calendar = tb.DateEntry(main_gui)
calendar.place(x=1200, y=10)

def clear_items():
    tree2.delete(*tree2.get_children())

clear_button = tb.Button(main_gui, text="Clear Items", command=clear_items)
clear_button.place(x=1060, y=610)

tb.Label(text="Listed Exercises").place(x=640, y=5)

tb.Label(text="Today's Exercises").place(x=1050, y=375)







main_gui.mainloop()