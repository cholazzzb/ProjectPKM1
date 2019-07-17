from tkinter import *
root = Tk()

root.title("Tick")
root.geometry("320x400")

AFTER = None
def tick():
    print ("tick!")
    global AFTER
    AFTER = root.after(1000, tick)

def key_pressed(event):
    if event.keysym == "Return":
        root.after_cancel(AFTER)

root.bind("<Key>", key_pressed)
root.after(1000, tick)
mainloop()
