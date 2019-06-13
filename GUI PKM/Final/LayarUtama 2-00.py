##### Import Library#####

import tkinter as tk
import tkinter.ttk as ttk

##### Import file lain sebagai OOP #####

##### Kelas aplikasi utama #####
class App(tk.Tk):
	def __init__(self):

        #### Konfigurasi Layar Utama ####
		tk.Tk.__init__(self)
		self.geometry('1280x800') # GUI geometry
		self.title('Smart Plastic Recycler') # GUI Title
        #self.configure(background='#FFFFFF') # White Color background

        #### Deklarasi Frame
		self.frame1 = ttk.Frame(self)
		self.frame1.grid(sticky = 'nsew')

		self.next_btn = ttk.Button(self.frame1,text = 'Next',command = self.frame2_visible)
		self.next_btn.grid(sticky = 'se')

		self.frame2 = ttk.Frame(self)

		self.back_btn = ttk.Button(self.frame2,text = 'Back',command = self.frame1_visible)
		self.back_btn.grid(column = 2,sticky = 'sw')

	def frame2_visible(self):
		self.frame1.grid_remove()
		self.frame2.grid(sticky = 'nsew')

	def frame1_visible(self):
		self.frame2.grid_remove()
		self.frame1.grid(sticky = 'nsew')

App().mainloop()
