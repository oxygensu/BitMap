from tkinter import *

BoardValue = ["-","-","-","-","-","-","-","-","-"]

window = Tk()
window.title("Noughts And Crosses")
window.geometry("10x200")

v = StringVar()
Label(window, textvariable=v,pady=10).pack()
v.set("Noughts And Crosses")

btn=[]

class BoardButton():
    def __init__(self,row_frame,b):
        global btn
        self.position= len(btn)
        btn.append(Button(row_frame, text=b, relief=GROOVE, width=2,command=lambda: self.callPlayMove()))
        btn[self.position].pack(side="left")

    def callPlayMove(self):
        PlayMove(self.position)

def DrawBoard():
    for i, b in enumerate(BoardValue):
        global btn
        if i%3 == 0:
            row_frame = Frame(window)
            row_frame.pack(side="top")
        BoardButton(row_frame,b)
        #btn.append(Button(row_frame, text=b, relief=GROOVE, width=2))
        #btn[i].pack(side="left")

def UpdateBoard():
    for i, b in enumerate(BoardValue):
        global btn
        btn[i].config(text=b)

def PlayMove(positionClicked):
    if BoardValue[positionClicked] == '-':
        BoardValue[positionClicked] = "X"
    else:
        BoardValue[positionClicked] = '-'
    UpdateBoard()

DrawBoard()
window.mainloop()