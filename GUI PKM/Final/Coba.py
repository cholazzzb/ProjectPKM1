#### Import Module
from tkinter import *

#### Root
root = Tk()

### Left Side

## Icon

# OK Icon
iconOK = PhotoImage(file="Cancel.jpg")
OKpanel = Label(root, image=iconOK)
OKpanel.grid(row=1, column=0, sticky='w')


#### Root Execution
root.mainloop()
