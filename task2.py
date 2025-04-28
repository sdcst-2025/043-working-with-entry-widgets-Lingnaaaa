#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk
import math
win=tk.Tk()
eoutput=tk.StringVar()
eoutput.set("   is the length")

def clickFuncation(e):
    print(e)
    side1 = e1.get()
    side1=float(side1)
    side2 = e2.get()
    side2=float(side2)
    side3 = math.sqrt(side1**2+side2**2)
    e3.insert(0,side3)

l1=tk.Label(win,width=15,text="Side1")
e1=tk.Entry(win,width=15)
l2=tk.Label(win,text="Side2")
e2=tk.Entry(win,width=15)
b1=tk.Button(win,text="Click for solve\n The length of the longer side")
b1.bind('<Button>',clickFuncation)
e3=tk.Entry(win,width=30,textvariable=eoutput)

l1.pack()
e1.pack()
l2.pack()
e2.pack()
b1.pack()
e3.pack()
win.mainloop()




