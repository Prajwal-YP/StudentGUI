import exp4 as tool
from tkinter import *

def create():
    b1 = Button(w,text="Add Student",command=addition)
    b2 = Button(w,text="View Students")
    b1.grid(row=3,column=1)
    return b1,b2
    
def modadd(l3,l4,l5,e1,e2,e3,b3,n,a,g):
    l3.destroy()
    l4.destroy()
    l5.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    b3.destroy()
    tool.add(n,a,g)
    create()

def addition():
    b1.destroy()
    l3=Label(w,text="Name:")
    l3.grid(row=3,column=0)
    e1=Entry(w)
    e1.grid(row=3,column=1,columnspan=2)
    l4=Label(w,text="Age:")
    l4.grid(row=4,column=0)
    e2=Entry(w)
    e2.grid(row=4,column=1,columnspan=2)
    l5=Label(w,text="Gender:")
    l5.grid(row=5,column=0)
    e3=Entry(w)
    e3.grid(row=5,column=1,columnspan=2)
    b3=Button(w,text='submit',command=lambda:modadd(l3,l4,l5,e1,e2,e3,b3,e1.get(),e2.get(),e3.get()))
    b3.grid(row=6,column=2)    
    


    

w = Tk()
w.title("Student Data")
l1 = Label(w,text="************MENU************")
l1.grid(row=0,column=0,columnspan=3)
l2 = Label(w,text="P R A J W A L   Y   P")
l2.grid(row=1,column=0,columnspan=3)
b1,b2=create()

mainloop()
