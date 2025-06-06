"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk
w=tk.Tk()


def run(e):
    print(e)
    n1 = e1.get()
    n1=float(n1)
    n2 = e2.get()
    n2=float(n2)
    try:
        if (n1**2)-(4*n2)>=0:
            x=(0-n1+((n1**2)-(4*n2))**0.5)/2
            x2=(0-n1-((n1**2)-(4*n2))**0.5)/2
            x=round(x,2)
            x2=round(x2,2)
            e3.delete(0,tk.END) 
            e4.delete(0,tk.END)
            s1=f"x - {x}" if x>=0 else f"x + {abs(x)}"
            s2=f"x - {x2}" if x2>=0 else f"x + {abs(x2)}"
            e3.insert(0,s1)
            e4.insert(0,s2)
    except:
        print("error,try anther number")

    

l0=tk.Label(w,text="ax^2+bx+c")
l1=tk.Label(w,text="Number 1")
e1=tk.Entry(w,width=15)
l2=tk.Label(w,text="Number 2")
e2=tk.Entry(w,width=15)
b1=tk.Button(w,text="Click for solve")
b1.bind('<Button>',run)
e3=tk.Entry(w,width=30)
e4=tk.Entry(w,width=30)

l0.grid(row=0,column=0,columnspan=2)
l1.grid(row=1,column=0)
e1.grid(row=1,column=1)
l2.grid(row=2,column=0)
e2.grid(row=2,column=1)
b1.grid(row=3,column=0,columnspan=2)
e3.grid(row=4,column=1)
e4.grid(row=5,column=1)
w.mainloop()