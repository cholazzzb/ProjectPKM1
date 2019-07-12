def changeframe(frame, state):
    if state == True:
        state=False
        return frame.grid_forget()
    else:
        state=True
        return frame.grid()

def show_label(self):
    self.label.lift(self.frame)

def hide_button(event):
    event.widget.grid_remove()
    #self.label.lower(self.frame)

def xprint():
    print("Hello World")
    
    
    
### Kedepannya keliatannya ini ditaro di SPRGUI.py
#----- Event State 2
#def s2_OK():
    