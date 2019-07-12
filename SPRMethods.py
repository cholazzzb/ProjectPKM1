def changeframe(frame, state):
    if state == True:
        state=False
        return frame.grid_forget()
    else:
        state=True
        return frame.grid()

def show_label(self, event=None):
    self.label.lift(self.frame)

def hide_label(self, event=None):
    self.label.lower(self.frame)

def xprint():
    print("Hello World")