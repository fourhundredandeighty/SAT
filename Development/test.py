from tkinter import Tk, Label
from PIL import ImageTk, Image

# Create a Tkinter window
root = Tk()

# Open the image using PIL
image = Image.open("image.png")

# Resize the image
resized_image = image.resize((100, 100))

# Convert the PIL image object to a Tkinter image object
tk_image = ImageTk.PhotoImage(resized_image)

# Display the image on a Tkinter label
label = Label(root, image=tk_image)
label.pack()

# Run the Tkinter main loop
root.mainloop()