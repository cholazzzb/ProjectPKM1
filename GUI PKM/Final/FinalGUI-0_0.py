#### Import Module
from tkinter import *

#### Root
root = Tk()

#### Root Configuration
root.title('Smart Plastic Recycler') # GUI Title
root.configure(background='#FFFFFF') # White Color background

### Button Configuration

### Upper Side
Label(root, text="Selamat Datand di Smart Plastic Recycler").grid(row=0, column=0, sticky='we')

### Left Side

## Icon
# Create an Icon bar
icon_bar = Frame(root, height=25, background='light sea green')
icon_bar.pack(expand='no', fill='y')

# OK Icon
'''
iconOK = PhotoImage(file="Cancel.jpg")
OKpanel = Label(root, image=iconOK)
OKpanel.grid(row=1, column=0, sticky='w')
'''



## Button
Button(root, text='OK').grid(row=1, column=0, sticky='w')
Button(root, text='BACK').grid(row=2, column=0, sticky='w')
Button(root, text='CANCEl').grid(row=3, column=0, sticky='w')
Button(root, text='HELP').grid(row=4, column=0, sticky='w')

#### Root Execution
root.mainloop()
