from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("Exercise Planner")
root.geometry("600x600")

date = tb.DateEntry(root)
date.place(x=360, y=20)

# exercises

root.mainloop()