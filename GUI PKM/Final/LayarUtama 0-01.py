#### Import Module ####
import tkinter as tk# For root
from PIL import ImageTk, Image
import tkinter.messagebox # For tkMessageBox
#import os
#from .images import iconCancel
#from PIL import ImageTk,Image

#### Root ####
root = tk.Tk()

#### Root Configuration
root.title('Smart Plastic Recycler') # GUI Title
root.configure(background='#FFFFFF') # White Color background

#### Frame Configuration ####
upper_frame = tk.Frame(root, height=250, width= 1000, background='light sea green')
upper_frame.grid(row=0, column=0, rowspan=2, columnspan=4, sticky='we')

left_frame = tk.Frame(root, height=450, width=250, background='khaki')
left_frame.grid(row=2, column=0, rowspan=6, columnspan=2, sticky='w')

right_frame = tk.Frame(root, height=450, width=750, background="#FFFFFF")
right_frame.grid(row=2, column=2, sticky='es')

##### Debugging
#tk.Button(root, text='BACK').grid(row=4, column=2, sticky='w')

### Button Configuration ###

## Callback Method ##

# MessageBox 1 : ThankYou
def thankYouCallBack():
    messagebox.showinfo("Thank You", "ThankYou")

## Icon ##

## OK Icon

# Make the canvas
#canvas = tk.Canvas(root, width = 50, height = 500, bd=0, bg='#FFFFFF')
#canvas.grid(row=1, column=0, sticky='we')

# Input the image
#imgOK = tk.PhotoImage(file='OK.gif')
#img = tk.PhotoImage(file="Back.gif")
#img = tk.PhotoImage(file="Cancel.gif")
#img = tk.PhotoImage(file="Help.gif")

img = ImageTk.PhotoImage(Image.open('OK.jpg'))
panel = Label(left_frame, image = img)
panel.grid(row=1, column=0, sticky='we')

#canvas.create_image(10,10, anchor=NW, image=imgOK)

## Button ##
tk.Button(left_frame, text='OK', command=thankYouCallBack).grid(row=3, column=1, sticky='w')
#tk.Button(left_frame, text='BACK').grid(row=4, column=1, sticky='w')
#tk.Button(left_frame, text='CANCEL').grid(row=5, column=1, sticky='w')
#tk.Button(left_frame, text='HELP').grid(row=6, column=1, sticky='w')

### Upper Side
#tk.Label(icon_bar, text="Selamat Datand di Smart Plastic Recycler").grid(row=2, column=0, sticky='we')

### Left Side

#### Root Execution ####
root.mainloop()
