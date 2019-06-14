##### Import Library#####

import tkinter as tk
import tkinter.ttk as ttk


##### Import file lain sebagai Modular #####

import SPRMethods as M
import SPRRFID as RFID
import SPRInternet as Inet

##### Deklarasi Variable Global #####
upper_frame_state = True
left_frame_state = True
right_frame_state = True

##### Kelas aplikasi utama #####
# parameter yang belum :  , icommand
def SPRbutton(iframe, irow, icolumn, itext, icommand):
    button = tk.Button(iframe, text = itext, background='#FFFFFF', activebackground='#A1FCA3', borderwidth='1', width=10, height=3, pady=5, command=icommand).grid(
    row=irow, column=icolumn, sticky='w')
    return button

#tk.Button(left_frame, text='OK', background='#FFFFFF', activebackground='#A1FCA3' ,borderwidth='1', width=10, height=3, pady=5, command=OKCallBack).grid(
#row=3, column=1, sticky='w')
#tk.Button(left_frame, text='Kembali', background='#FFFFFF', activebackground='#A1FCA3', borderwidth='1', width=10, height=3, pady=5, command=kembaliCallBack).grid(
#row=4, column=1, sticky='w')
#tk.Button(left_frame, text='Batal', background='#FFFFFF', activebackground='#A1FCA3', borderwidth='1', width=10, height=3, pady=5, command=batalCallBack).grid(
#row=5, column=1, sticky='w')
#tk.Button(left_frame, text='Bantuan', background='#FFFFFF', activebackground='#A1FCA3', borderwidth='1', width=10, height=3, pady=5, command=bantuanCallBack).grid(
#row=6, column=1, sticky='w')


class App(tk.Tk):
    def __init__(self):

        #### Konfigurasi Layar Utama ####
        tk.Tk.__init__(self)
        self.geometry('1280x600') # GUI geometry. Harusnya 1280x800
        self.title('Smart Plastic Recycler') # GUI Title
        self.configure(bg='#FFFFFF') # White Color background

        #### Deklarasi Frame
        self.upper_frame = ttk.Frame(self, height=250, width= 1000)
        self.upper_frame.grid(row=0, column=0, rowspan=2, columnspan=4, sticky='we')

        self.left_frame = ttk.Frame(self, height=450, width=250)
        self.left_frame.grid(row=2, column=0, rowspan=6, columnspan=2, sticky='w')

        self.right_frame = ttk.Frame(self, height=450, width=750)
        self.right_frame.grid(row=2, column=2, stick='es')

        #### Deklarasi Button di Frame Kiri
        SPRbutton(self.left_frame, 3, 1, "OK", M.changeframe(self.right_frame, right_frame_state))
        SPRbutton(self.left_frame, 4, 1, "Kembali", M.changeframe(self.right_frame, right_frame_state))
        SPRbutton(self.left_frame, 5, 1, "Batal", M.changeframe(self.right_frame, right_frame_state))
        SPRbutton(self.left_frame, 6, 1, "Bantuan", M.changeframe(self.right_frame, right_frame_state))

        #### Deklarasi label
        ttk.Label(self.upper_frame, text="SELAMAT DATANG !!!").grid(row=1, column=2)

        # Temporary Button
        SPRbutton(self.right_frame, 3, 4, "Frame 1", M.changeframe(self.left_frame, left_frame_state))


		#self.next_btn = ttk.Button(self.frame1,text = 'Next',command = self.frame2_visible)
		#self.next_btn.grid(sticky = 'se')

        self.frame2 = ttk.Frame(self)

		#self.back_btn = ttk.Button(self.frame2,text = 'Back',command = self.frame1_visible)
		#self.back_btn.grid(column = 2,sticky = 'sw')

    def frame2_visible(self):
		#self.frame1.grid_remove()
        self.frame2.grid(sticky = 'nsew')

    def frame1_visible(self):
        self.frame2.grid_remove()
		#self.frame1.grid(sticky = 'nsew')

App().mainloop()
