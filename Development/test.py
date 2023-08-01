from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x750")

#Create a canvas
canvas= Canvas(win)
canvas.place(x=10, y=10)

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("image.png"))

#Add image to the Canvas Items
canvas.create_image(100,100,anchor=NW,image=img)

win.mainloop()