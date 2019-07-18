#----- Import Library -----#
from tkinter import font
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
import time
from PIL import ImageTk, Image

root = tk.Tk()

logo_ori = Image.open("iconBantuan.png")#buat logo sesuai keperluan ukuran
logo60 = logo_ori.resize((60, 60), Image.ANTIALIAS)
logo60.save("Bantuan.png")

logo60 = tk.PhotoImage(file="iconBantuan.png") #import ke py
logo = ttk.Label(root, image=logo60, background='white')
logo.grid(column=0,row=0)

root.mainloop()