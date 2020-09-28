import tkinter as tk
import os
import A429Label
window = tk.Tk()
window.title("Bit Map Test")
window.geometry("500x500")
btn = []
bits32 = A429Label.Union()

def draw():
    for i in range(32):
        b = tk.Button(window, text="Bit" + str(i+1) + ":0", command=lambda i=i: clickButton(i))
        b.grid(row = 1, column = i+1)
        btn.append(b)
    
def clickButton(argIndex):
    global btn
    if btn[argIndex]['text'] == "Bit" + str(argIndex+1) + ":0":
        btn[argIndex]['text'] = "Bit" + str(argIndex+1) + ":1"
        btn[argIndex]['background'] = "green"
        refresh_bits(argIndex+1, 1)
    else:
        btn[argIndex]['text'] = "Bit" + str(argIndex+1) + ":0"
        btn[argIndex]['background'] = "white"
        refresh_bits(argIndex+1, 0)

def refresh_bits(argIndex, val):
    if argIndex == 1:
        bits32.label.bit1 = val
    elif argIndex == 2:
        bits32.label.bit2 = val
    elif argIndex == 3:
        bits32.label.bit3 = val
    elif argIndex == 4:
        bits32.label.bit4 = val
    elif argIndex == 5:
        bits32.label.bit5 = val
    elif argIndex == 6:
        bits32.label.bit6 = val
    elif argIndex == 7:
        bits32.label.bit7 = val
    elif argIndex == 8:
        bits32.label.bit8 = val
    elif argIndex == 9:
        bits32.label.bit9 = val
    elif argIndex == 10:
        bits32.label.bit10 = val
    elif argIndex == 11:
        bits32.label.bit11 = val
    elif argIndex == 12:
        bits32.label.bit12 = val
    elif argIndex == 13:
        bits32.label.bit13 = val
    elif argIndex == 14:
        bits32.label.bit14 = val
    elif argIndex == 15:
        bits32.label.bit15 = val
    elif argIndex == 16:
        bits32.label.bit16 = val
    elif argIndex == 17:
        bits32.label.bit17 = val
    elif argIndex == 18:
        bits32.label.bit18 = val
    elif argIndex == 19:
        bits32.label.bit19 = val
    elif argIndex == 20:
        bits32.label.bit20 = val
    elif argIndex == 21:
        bits32.label.bit21 = val
    elif argIndex == 22:
        bits32.label.bit22 = val
    elif argIndex == 23:
        bits32.label.bit23 = val
    elif argIndex == 24:
        bits32.label.bit24 = val
    elif argIndex == 25:
        bits32.label.bit25 = val
    elif argIndex == 26:
        bits32.label.bit26 = val
    elif argIndex == 27:
        bits32.label.bit27 = val
    elif argIndex == 28:
        bits32.label.bit28 = val
    elif argIndex == 29:
        bits32.label.bit29 = val
    elif argIndex == 30:
        bits32.label.bit30 = val
    elif argIndex == 31:
        bits32.label.bit31 = val
    elif argIndex == 32:
        bits32.label.bit32 = val
    label['text'] = str(f"{bits32.asbyte:#0{0}x}")

def reset_bits():
    for i in range(32):
        refresh_bits(i + 1, 0)
        btn[i]['text'] = "Bit" + str(i+1) + ":0"
        btn[i]['background'] = "white"

draw()
label = tk.Label(window, text=str(f"{bits32.asbyte:#0{0}x}"))
label.grid()
clearBtn = tk.Button(window, text="Reset to 0", command=reset_bits)
clearBtn.grid()
window.mainloop()