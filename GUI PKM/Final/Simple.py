# ---------Import----------
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library

# ---------Settings--------
white='#FFFFFF' # variable untuk warna background = putih
green='#A1FCA3' # variable untuk warna hijau
root = tk.Tk()
root.title('Smart Plastic Recycler') # GUI Title
root.configure(background='#FFFFFF') # White Color background
root.geometry('1280x600')
root.resizable(height=False, width=False)


# ---------Variables----------
outputData = tk.StringVar()
value=5



# --------Frames---------
logo=tk.Frame(root, width=1280, height=100)
logo.pack(side='top')
button=tk.Frame(root)
button.pack(side='left')
isi=tk.Frame(root, width=1280, height=500, background='light sea green')
isi.pack(side='left')



# --------Functions---------





# ---------Buttons----------
tk.Button(button, text="OK", width=10, activebackground=green).pack(side='top')
tk.Button(button, text="Kembali", width=10, activebackground=green).pack(side='top')
tk.Button(button, text="Batal", width=10, activebackground=green).pack(side='top')
tk.Button(button, text="Bantuan", width=10, activebackground=green).pack(side='top')



# ---------Entry+Labels---------
# Label Sambutan
label_sambutan=tk.Label(logo, text='Selamat Datang !!!', pady=40, background=white)
label_sambutan.pack(fill='both', side='top')
label_sambutan.config(font=("Courier", 54))

# Entry Output
data=tk.Entry(isi, textvariable=outputData, width=200)
data.pack(fill='x', side='right')
outputData.set(value)


# ---------Execution----------
root.mainloop()
