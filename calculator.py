from tkinter import *
from time import sleep

master = Tk()
master.title("Calculator")

w=Canvas(master,width=500,height=500)

p="                    "

def add():
    l7=Label(master,text=p,width=20)
    l7.grid(row=18,column=2)
    a=float(e1.get())
    b=float(e2.get())
    l7=Label(master,text=a+b,width=20)
    l7.grid(row=18,column=2)

def sub():
    l7=Label(master,text=p,width=20)
    l7.grid(row=18,column=2)
    a=float(e1.get())
    b=float(e2.get())
    l7=Label(master,text=a-b,width=20)
    l7.grid(row=18,column=2)
    
def prdt():
    l7=Label(master,text=p,width=20)
    l7.grid(row=18,column=2)
    a=float(e1.get())
    b=float(e2.get())
    l7=Label(master,text=a*b,width=20)
    l7.grid(row=18,column=2)
   
def quot():
    l7=Label(master,text=p,width=20)
    l7.grid(row=18,column=2)
    a=float(e1.get())
    b=float(e2.get())
    l7=Label(master,text=a/b,width=20)
    l7.grid(row=18,column=2)

def rem():
    l7=Label(master,text=p,width=20)
    l7.grid(row=18,column=2)
    a=float(e1.get())
    b=float(e2.get())
    l7=Label(master,text=a%b,width=20)
    l7.grid(row=18,column=2)

def pow():
    l7=Label(master,text=p,width=20)
    l7.grid(row=18,column=2)
    a=float(e1.get())
    b=float(e2.get())
    l7=Label(master,text=a**b,width=20)
    l7.grid(row=18,column=2)

e1 = Entry(master)
e1.grid(row=0,column=2)
e2 = Entry(master)
e2.grid(row=3,column=2)


l1 = Label(master,text="First No.:",justify = LEFT)
l1.grid(row=0,column=0)

l2 = Label(master,text="Second No.:",justify = LEFT)
l2.grid(row=3,column=0)

l3 = Label(master,text="Answer:",justify = LEFT)
l3.grid(row=18,column=0)

l4 = Label(master,text=":")
l4.grid(row=0,column=1)

l5 = Label(master,text=":")
l5.grid(row=3,column=1)

l6 = Label(master,text=":")
l6.grid(row=18,column=1)

b1 = Button(master,text="+ ",command = add,width=19,bd=5)
b1.grid(row = 9,column = 0)

b2 = Button(master,text="- ",command = sub,width=19,bd=5)
b2.grid(row = 9,column = 2)

b3 = Button(master,text=" * ",command = prdt,width=19,bd=5)
b3.grid(row = 12,column = 2)

b4 = Button(master,text="/ ",command = quot,width=19,bd=5)
b4.grid(row = 12,column = 0)

b5 = Button(master,text="^",command = pow,width=19,bd=5)
b5.grid(row = 15,column = 0)

b6 = Button(master,text="remainder",command = rem,width=19,bd=5)
b6.grid(row = 15,column = 2)

mainloop()
