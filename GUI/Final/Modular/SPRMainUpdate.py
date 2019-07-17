#----- Import Library -----#
from tkinter import font
from tkinter import messagebox
import tkinter as tk # For root
import tkinter.ttk as ttk # More modern library
import time
from PIL import ImageTk, Image

#--- Firebase
import sys
sys.path.append('/usr/lib/python2.7/dist-packages/') #thonny pakai Python3, python path di term 2.7
from firebase import firebase

#----- Import file lain sebagai Modular -----#
import SPRMethods as M
import SPRRFID as RFID
import SPRInternet as Inet

#import SPRGUI as GUI

#----- Deklarasi Variable Global -----#
global eventState
eventState=1

# ----- Settings -----#
##Warna
white='#FFFFFF' # variable untuk warna background = putih
green='#A1FCA3' # variable untuk warna hijau

## Build root
blue='#A1FCA5'
root = tk.Tk()
root.title('Smart Plastic Recycler') # GUI Title
root.configure(background='#000000') # White Color background
root.resizable(height=False, width=False) #fullsscreen
root.wm_attributes('-fullscreen','true') #fullscreen

#----------Constants-----------
logo_size=350 #ukuran logo
lcd_width=1280 #ukuran lcd
lcd_height=800
tebal_garis_pembatas=7 #tebal garis ijo
space_size=100 #ukuran space di kanan untuk estetika, coba ganti tes_spacing dg 'green'
tes_spacing='green' #indikasi tebal spacing
pady_button=6 #padding/jeda tiap kolom/row thd button
padx_button=100
pad_garis=40

# ---------Style-------- #pengaturan ui perlu style, gabisa dikasih argumen langsung di objek
s = ttk.Style()
s.configure('white.TFrame', background='white')
s.configure('green.TFrame', background='green')
s.configure('blue.TFrame', background='blue')
s.configure('button1.TButton', background='white', font='helvetica 22')
font_judul = font.Font(family='Helvetica', size=64, weight='bold')#define font style
font_normal = font.Font(family='Helvetica', size=32, weight='bold')

#---------Variables---------- #to be used later
v_id = '12312312'
v_nama = 'Nic'
v_saldo = '75000'
v_jumlahBotol = '0'
v_jenisBotol = 'Botol Besar'
v_saldoTambahan = 'Rp 150'
v_saldoAkhir = '18150'

# delay
delay=ttk.Entry(root)

#----- Aplikasi Utama -----#
#--------Mainframe-------- #inisiasi frame utama
content=ttk.Frame(root, style='white.TFrame')
content.grid(column=0, row=0)


# --------Frames--------- #frame2 yang dipakai
#logo
frame_logo=ttk.Frame(content, width=lcd_width, style='white.TFrame')
# height=logo_size,
frame_logo.grid(column=0, row=0, columnspan=3)

#label
frame_label=ttk.Frame(content, width=lcd_width, height=lcd_height-tebal_garis_pembatas-40, style='green.TFrame')
frame_label.grid(column=0, row=1, columnspan=3)

#button
frame_button=ttk.Frame(content, width=lcd_width, height=40, style='white.TFrame')
frame_button.grid(column=0, row=2, columnspan=3)


#---------Masukin Gambar----------
logo_file = tk.PhotoImage(file="logo_resized.png") #import ke py
iconBantuan = tk.PhotoImage(file="iconBantuan.png")
logoKecil = tk.PhotoImage(file="logo60.png")
    

## ----- Fungsi -----

#Klo tombol bantuan ditekan
def bantu():
    messagebox.showinfo(message='Untuk bantuan silahan hubungi Dartwin 08xxxxxxxxxx')

def mulai():
    
    global logo
    logo = ttk.Label(frame_logo, image=logo_file, background='white')
    logo.grid(column=0,row=0)

    global judul
    judul = ttk.Label(frame_logo, text='Selamat Datang!', font=font_judul, background='white')
    judul.grid(column=1,row=0)

    global spacing
    spacing=ttk.Frame(frame_logo, width=space_size, style=tes_spacing+'.TFrame')
    spacing.grid(column=2, row=0)
    
    global e_mulai
    e_mulai = ttk.Label(frame_label, text="Silahkan klik tombol mulai lalu tempelkan kartu RFID anda!", width=30, background='blue', font=font_normal)
    e_mulai.grid(column=0, row=0, pady=pady_button, padx=padx_button)
    
    global button_mulai
    button_mulai=ttk.Button(frame_label, text="Mulai", width=10, style='button1.TButton', command= lambda :[RFID.checkId(), s1_mulai()] )
    button_mulai.grid(column=0,row=1, pady=150, padx=padx_button)
    
def s1_mulai():
    v_id = "Id = " + str(RFID.getId())
    global v_namaAja
    v_namaAja = str(Inet.get(Inet.makeId(str(RFID.getId())))["nama"])
    v_nama = "Nama = " + v_namaAja
    v_saldo = "Saldo = " + str(Inet.get(Inet.makeId(str(RFID.getId())))["saldo"])
    
    button_mulai.grid_remove()
    e_mulai.grid_remove()
    logo.grid_remove()
    judul.grid_remove()
    #Ilangin bagian atas
    
    ##--------Frame Logo----------
    global logoLabel
    logoLabel = ttk.Label(frame_label, image=logoKecil, background='white')
    logoLabel.grid(column=0,row=0, sticky='w')
    
    global buttonBantuan
    buttonBantuan = ttk.Button(frame_label, image=iconBantuan, style='button1.TButton')
    buttonBantuan.grid(column=2,row=0, sticky='e')
    
    ##---------Frame label----------
    global e_apakah
    e_apakah = ttk.Label(frame_label, text ="Apakah datanya benar?", font=font_normal)
    e_apakah.grid(column=1, row=1, pady=pady_button, padx=padx_button)
    
    global e_id
    e_id = ttk.Label(frame_label, text=v_id, width=30, background='blue', font=font_normal)
    e_id.grid(column=1, row=2, pady=pady_button, padx=padx_button)

    global e_nama
    e_nama = ttk.Label(frame_label, text=v_nama, width=30, background='blue', font=font_normal)
    e_nama.grid(column=1, row=3, pady=pady_button, padx=padx_button)

    global e_saldo
    e_saldo = ttk.Label(frame_label, text=v_saldo, width=30, background='blue', font=font_normal)
    e_saldo.grid(column=1, row=4, pady=pady_button, padx=padx_button)
    
    global buttonKembali
    buttonKembali = ttk.Button(frame_label, text="Salah", style='button1.TButton', command= lambda:[balikKeAwal(), mulai()])
    buttonKembali.grid(column=0,row=5)
    
    global buttonOk
    buttonOk = ttk.Button(frame_label, text = "Benar", style='button1.TButton' , command= lambda : [Inet.update(Inet.makeId(str(RFID.getId())), "botol kecil"), tambahLagi()])
    buttonOk.grid(column=2,row=5)
    
def balikKeAwal():
    logoLabel.grid_remove()
    buttonBantuan.grid_remove()
    e_apakah.grid_remove()
    e_id.grid_remove()
    e_nama.grid_remove()
    e_saldo.grid_remove()
    buttonKembali.grid_remove()
    buttonOk.grid_remove()
    
    
def tambahLagi():
    e_apakah.grid_remove()
    e_id.grid_remove()
    e_nama.grid_remove()
    e_saldo.grid_remove()
    buttonOk.grid_remove()
    buttonKembali.grid_remove()
    
    global label_state2_1
    label_state2_1 = ttk.Label(frame_label, text='Silahkan masukkan botol ke lubang masuk botol', width=30, background='white', font=font_normal)
    #, font=font_judul
    label_state2_1.grid(column=1,row=1)
    
    global buttonUdah
    buttonUdah = ttk.Button(frame_label, text = "Udah", style='button1.TButton', command= lambda: tambah())
    buttonUdah.grid(column=2,row=2)
    
    delay.after(10000, lambda:[s3_sudah(), label_state2_1.grid_remove(), buttonUdah.grid_remove()])
    
    
def tambah():
    label_state2_1.grid_remove()
    buttonUdah.grid_remove()
    
    global lagi
    lagi = ttk.Label(frame_label, text='Apakah anda masih ingin memasukkan sampah botol plastik?', width=30, background='white', font=font_normal)
    #, font=font_judul
    lagi.grid(column=1,row=1)
    
    global buttonYa
    buttonYa = ttk.Button(frame_label, text = "Ya", style='button1.TButton', command= lambda: loopUWU())
    buttonYa.grid(column=2,row=2)
    
    global buttonGa
    buttonGa = ttk.Button(frame_label, text = "Tidak", style='button1.TButton' , command= lambda : [Inet.update(Inet.makeId(str(RFID.getId())), "botol kecil"), s3_sudah(), khusus()])
    buttonGa.grid(column=0,row=2)
    
def loopUWU():
    lagi.grid_remove()
    buttonYa.grid_remove()
    buttonGa.grid_remove()
    
    global label_state2_1
    label_state2_1 = ttk.Label(frame_label, text='Silahkan masukkan botol ke lubang masuk botol', width=30, background='white', font=font_normal)
    #, font=font_judul
    label_state2_1.grid(column=1,row=1)
    
    global buttonUdah
    buttonUdah = ttk.Button(frame_label, text = "Udah", style='button1.TButton', command= lambda: tambah())
    buttonUdah.grid(column=2,row=2)
    
    delay.after(10000, lambda:[mulai(), label_state2_1.grid_remove(), buttonUdah.grid_remove()])
        
def khusus():
    lagi.grid_remove()
    e_apakah.grid_remove()
    e_id.grid_remove()
    e_nama.grid_remove()
    e_saldo.grid_remove()
    label_state2_1.grid_remove()
    buttonYa.grid_remove()
    buttonGa.grid_remove()

def s3_sudah():
        
    v_jenisBotol = "Jenis Botol = Botol Kecil"
    v_saldoTambahan = "Saldo Tambahan = " + Inet.liatSaldoTambahan()
    v_saldoAkhir = "Saldo Akhir = " + Inet.liatSaldoAkhir()
    
    global e_banyakBotol
    e_banyakBotol = ttk.Label(frame_label, text=v_jumlahBotol, width=30, background='blue',font=font_normal)
    e_banyakBotol.grid(column=0, row=1, pady=pady_button, padx=padx_button)    

    global e_jenisBotol
    e_jenisBotol = ttk.Label(frame_label, text=v_jenisBotol, width=30, background='blue', font=font_normal)
    e_jenisBotol.grid(column=0, row=2, pady=pady_button, padx=padx_button)

    global e_saldoTambahan
    e_saldoTambahan = ttk.Label(frame_label, text=v_saldoTambahan, width=30, background='blue', font=font_normal)
    e_saldoTambahan.grid(column=0, row=3, pady=pady_button, padx=padx_button)

    global e_saldoAkhir
    e_saldoAkhir = ttk.Label(frame_label, text=v_saldoAkhir, width=30, background='blue',font=font_normal)
    e_saldoAkhir.grid(column=0, row=4, pady=pady_button, padx=padx_button)
 
    global buttonUpdate
    buttonUpdate = ttk.Button(frame_label, text = "Lanjut", style='button1.TButton' , command= lambda : makasi())
    buttonUpdate.grid(column=2,row=5)

def makasi():
    logoLabel.grid_remove()
    buttonBantuan.grid.remove()
    e_banyakBotol.grid_remove()    
    e_jenisBotol.grid_remove()
    e_saldoTambahan.grid_remove()
    e_saldoAkhir.grid_remove()
    buttonUpdate.grid_remove()
    
    global e_makasi
    e_makasi = ttk.Label(frame_label, text="Terimakasih atas kerjasama " + v_namaAja + " semoga dunia menjadi lebih indah =)", font=font_normal, background='blue')
    e_makasi.grid(column=1, row=1)
    delay.after(5000,lambda:[ulang(), mulai()])

def ulang():
    e_makasi.grid_remove()
    e_jenisBotol.grid_remove()
    e_saldoTambahan.grid_remove()
    e_saldoAkhir.grid_remove()

##----- Event 1 -----#

#frame sisa
fSisa = lcd_height-logo_size-tebal_garis_pembatas-2*pad_garis-2*pady_button-4*10
frame_button=ttk.Frame(content, width=lcd_width, height=fSisa, style='white.TFrame')
frame_button.grid(column=0, row=6, columnspan=3)

mulai()

# ---------Execution----------

root.mainloop()


