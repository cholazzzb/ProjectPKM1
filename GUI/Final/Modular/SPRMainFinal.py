#----- Import Library -----#
from tkinter import font
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
v_jenisBotol = 'Botol Besar'
v_saldoTambahan = 'Rp 150'
v_saldoAkhir = '18150'

#----- Aplikasi Utama -----#
#--------Mainframe-------- #inisiasi frame utama
content=ttk.Frame(root, style='white.TFrame')
content.grid(column=0, row=0)


# --------Frames--------- #frame2 yang dipakai
#logo
frame_logo=ttk.Frame(content, width=lcd_width, height=logo_size, style='white.TFrame')
frame_logo.grid(column=0, row=0, columnspan=3)

#garis ijo pembatas
frame_garis=ttk.Frame(content, width=lcd_width, height=tebal_garis_pembatas, style='green.TFrame')
frame_garis.grid(column=0, row=1, columnspan=3, pady=pad_garis)

#label
frame_label=ttk.Frame(content, width=lcd_width, height=lcd_height-tebal_garis_pembatas-logo_size-40, style='green.TFrame')
frame_label.grid(column=0, row=2, columnspan=3)

#button
frame_button=ttk.Frame(content, width=lcd_width, height=40, style='white.TFrame')
frame_button.grid(column=0, row=3, columnspan=3)


#---------Frame Logo----------
logo_ori = Image.open("Logo I-Smart Plastic Recycler-Dartwin-ITB.png")#buat logo sesuai keperluan ukuran
logo_resized = logo_ori.resize((logo_size, logo_size), Image.ANTIALIAS)
logo_resized.save("logo_resized.png")

logo_file = tk.PhotoImage(file="logo_resized.png") #import ke py
logo = ttk.Label(frame_logo, image=logo_file, background='white')
logo.grid(column=0,row=0)

judul = ttk.Label(frame_logo, text='Selamat Datang !!!', font=font_judul, background='white')
judul.grid(column=1,row=0)

spacing=ttk.Frame(frame_logo, width=space_size, style=tes_spacing+'.TFrame')
spacing.grid(column=2, row=0)

## ----- Fungsi -----
def mulai():
    global button_mulai
    button_mulai=ttk.Button(frame_label, text="Mulai", width=10, style='button1.TButton', command= lambda :s1_mulai() )
    button_mulai.grid(column=0,row=0, pady=pady_button, padx=padx_button)
    


def s1_mulai():
    global eventState
    eventState=2
    print(eventState)

    button_mulai.grid_remove()
    global tempelRFID
    tempelRFID = ttk.Label(frame_label, text="Silahkan tempelkan RFID anda sambil klik ya", font=font_normal, background='white')
    tempelRFID.grid(column=0, row=0)
    global button_ya
    button_ya=ttk.Button(frame_label,text='ya', width=10, style='button1.TButton', command= lambda :[RFID.checkId(), s2_ya()] )
    button_ya.grid(column=0, row=1)

def s2_ya():
    v_id = "Id = " + str(RFID.getId())
    v_nama = "Nama = " + str(Inet.get(Inet.makeId(str(RFID.getId())))["nama"])
    v_saldo = "Saldo = " + str(Inet.get(Inet.makeId(str(RFID.getId())))["saldo"])
    tempelRFID.grid_remove()
    button_ya.grid_remove()
     ##---------Frame label----------
    global e_id
    e_id = ttk.Label(frame_label, text=v_id, width=30, background='blue', font=font_normal)
    e_id.grid(column=0, row=0, pady=pady_button, padx=padx_button)

    global e_nama
    e_nama = ttk.Label(frame_label, text=v_nama, width=30, background='blue', font=font_normal)
    e_nama.grid(column=0, row=1, pady=pady_button, padx=padx_button)

    global e_saldo
    e_saldo = ttk.Label(frame_label, text=v_saldo, width=30, background='blue', font=font_normal)
    e_saldo.grid(column=0, row=2, pady=pady_button, padx=padx_button)

    global label_state2_1
    label_state2_1 = ttk.Label(frame_label, text='Silahkan masukan botol', width=30, background='white', font=font_normal)
    #, font=font_judul
    label_state2_1.grid(column=0,row=3)

    global button_sudah
    button_sudah=ttk.Button(frame_label,text='sudah', width=10, style='button1.TButton', command= lambda : [Inet.update(Inet.makeId(str(RFID.getId())), "botol kecil"), s3_sudah()] )
    button_sudah.grid(column=0, row=4)

def s3_sudah():
    e_id.grid_remove()
    e_nama.grid_remove()
    e_saldo.grid_remove()
    label_state2_1.grid_remove()
    button_sudah.grid_remove()
    
    
    v_jenisBotol = "Jenis Botol = Botol Kecil"
    v_saldoTambahan = "Saldo Tambahan = " + Inet.liatSaldoTambahan()
    v_saldoAkhir = "Saldo Akhir = " + Inet.liatSaldoAkhir()

    global label_proses


    global e_jenisBotol
    e_jenisBotol = ttk.Label(frame_label, text=v_jenisBotol, width=30, background='blue', font=font_normal)
    e_jenisBotol.grid(column=0, row=1, pady=pady_button, padx=padx_button)

    global e_saldoTambahan
    e_saldoTambahan = ttk.Label(frame_label, text=v_saldoTambahan, width=30, background='blue', font=font_normal)
    e_saldoTambahan.grid(column=0, row=2, pady=pady_button, padx=padx_button)

    global e_saldoAkhir
    e_saldoAkhir = ttk.Label(frame_label, text=v_saldoAkhir, width=30, background='blue',font=font_normal)
    e_saldoAkhir.grid(column=0, row=3, pady=pady_button, padx=padx_button)
    
    global button_selesai
    button_selesai=ttk.Button(frame_label,text='Selesai', width=10, style='button1.TButton', command= lambda : [ulang(), mulai()] )
    button_selesai.grid(column=0, row=4)

def ulang():
    e_jenisBotol.grid_remove()
    e_saldoTambahan.grid_remove()
    e_saldoAkhir.grid_remove()
    button_selesai.grid_remove()



##----- Event 1 -----#

#frame sisa
fSisa = lcd_height-logo_size-tebal_garis_pembatas-2*pad_garis-2*pady_button-4*10
frame_button=ttk.Frame(content, width=lcd_width, height=fSisa, style='white.TFrame')
frame_button.grid(column=0, row=4, columnspan=3)

mulai()

# ---------Execution----------

root.mainloop()

