"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk
win=tk.Tk()

def run(e):
    name = e1.get()
    l1.config(text=name)
    number = e3.get()
    l3.config(text=number)
    grade = e4.get()
    l4.config(text=grade)
    combine=f"name:{name},student number:{number},Grade:{grade}"
    e2.delete(0,tk.END)
    e2.insert(0,combine)

e1 = tk.Entry(win,width=15)
b1 = tk.Button(win, text="Click to change the text")
e2 = tk.Entry(win,width=40)
l1 = tk.Label(win, width=15, text="Name")
b1.bind("<Button-1>",run)
l3=tk.Label(win,width=15,text="Student Number")
e3=tk.Entry(win,width=15)
l4=tk.Label(win,width=15,text="Grade")
e4=tk.Entry(win,width=15)


l1.pack()
e1.pack()
l3.pack()
e3.pack()
l4.pack()
e4.pack()
b1.pack()
e2.pack()
win.mainloop()