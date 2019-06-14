#### Import Module ####
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
from PIL import ImageTk, Image
import tkinter.messagebox as tmb # For tkMessageBox
#import os
#from .images import iconCancel
#from PIL import ImageTk,Image

### Global Variable
upper_frame_state = True;
left_frame_state = True;
right_frame_state = True;

#### Root ####
root = tk.Tk()

#### Root Configuration
root.title('Smart Plastic Recycler') # GUI Title
root.configure(background='#FFFFFF') # White Color background
root.geometry('1280x800')

#### Frame Configuration ####
upper_frame = tk.Frame(root, height=250, width= 1000, background='light sea green')
upper_frame.grid(row=0, column=0, rowspan=2, columnspan=4, sticky='we')

#left_frame_null = tk.Frame(root, height=450, width=250, background='khaki')
#left_frame_null.grid(row=2, column=0, rowspan=6, columnspan=2, sticky='w')

left_frame = tk.Frame(root, height=450, width=250, background='khaki')
left_frame.grid(row=2, column=0, rowspan=6, columnspan=2, sticky='w')

right_frame = tk.Frame(root, height=450, width=750, background="#FFFFFF")
right_frame.grid(row=2, column=2, sticky='es')

##### Debugging
#tk.Button(root, text='BACK').grid(row=4, column=2, sticky='w')

## Method

'''
Input : Frame state yang diinginkan (1 = keliatan, 0 = sembunyi)
Output : Frame state jadi sesuai yang diinginkan sehingga frame keliatan atau tersembunyi
'''
def frameChange(frame, state):
    if state == '':
        state = 1
        return state
    else:
        state = 0
        return state



### Button Configuration ###

## Callback Method ##

# MessageBox 1 : ThankYou
def terimkasiCallBack():
    tmb.showinfo("Thank You", "ThankYou")

def OKCallBack():
    tmb.showinfo("OK", "OK")

def kembaliCallBack():
    tmb.showinfo("Kembali", "Kembali")

def batalCallBack():
    tmb.showinfo("Batal", "Batal")

def bantuanCallBack():
    tmb.showinfo("Bantuan", "Keterangan : \n OK = Lanjut \n Kembali = Kembali ke halaman sebelumnya \n Batal = Jika ingin membatalkan \n Bantuan = Memunculkan Layar Bantuan ")

## Icon ##

## OK Icon

# Make the canvas
canvas = tk.Canvas(root, width = 50, height = 500, bd=0, bg='#FFFFFF')
canvas.grid(row=1, column=0, sticky='we')

# Input the image
imgOK = tk.PhotoImage(file='OK.gif')
#img = tk.PhotoImage(file="Back.gif")
#img = tk.PhotoImage(file="Cancel.gif")
#img = tk.PhotoImage(file="Help.gif")

canvas.create_image(10,10, anchor=NW, image=imgOK)

## Temporary Icon ##
ttk.Label(left_frame, text='OK icon').grid(row=3, column=0, sticky='w')
ttk.Label(left_frame, text='Back Icon').grid(row=4, column=0, sticky='w')
ttk.Label(left_frame, text='CANCEL Icon').grid(row=5, column=0, sticky='w')
ttk.Label(left_frame, text='HELP Icon').grid(row=6, column=0, sticky='w')
# Icon Kapasitas
ttk.Label(upper_frame, text='icon kapasitas').grid(row=0, column=4)

## Temporary Logo ##
ttk.Label(upper_frame, text='LOGO').grid(row=1, column=1)



## Label in Upper Frame ##
ttk.Label(upper_frame, text='SELAMAT DATANG !!!').grid(row=1, column=2)




## Button in left_frame ##
tk.Button(left_frame, text='OK', background='#FFFFFF', activebackground='#A1FCA3' ,borderwidth='1', width=10, height=3, pady=5, command=OKCallBack).grid(
row=3, column=1, sticky='w')
tk.Button(left_frame, text='Kembali', background='#FFFFFF', activebackground='#A1FCA3', borderwidth='1', width=10, height=3, pady=5, command=kembaliCallBack).grid(
row=4, column=1, sticky='w')
tk.Button(left_frame, text='Batal', background='#FFFFFF', activebackground='#A1FCA3', borderwidth='1', width=10, height=3, pady=5, command=batalCallBack).grid(
row=5, column=1, sticky='w')
tk.Button(left_frame, text='Bantuan', background='#FFFFFF', activebackground='#A1FCA3', borderwidth='1', width=10, height=3, pady=5, command=bantuanCallBack).grid(
row=6, column=1, sticky='w')

### Upper Side
#tk.Label(icon_bar, text="Selamat Datand di Smart Plastic Recycler").grid(row=2, column=0, sticky='we')

### Left Side

#### Root Execution ####
root.mainloop()
