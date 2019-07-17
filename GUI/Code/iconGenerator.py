#----- Import Library -----#
from tkinter import font
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
import time
from PIL import ImageTk, Image

root = tk.Tk()

logo_ori = Image.open("Logo I-Smart Plastic Recycler-Dartwin-ITB.png")#buat logo sesuai keperluan ukuran
logo_resized = logo_ori.resize((60, 60), Image.ANTIALIAS)
logo_resized.save("logo_resized.png")

logo_file = tk.PhotoImage(file="logo_resized.png") #import ke py
logo = ttk.Label(root, image=logo_file, background='white')
logo.grid(column=0,row=0)

root.mainloop()