from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry("720x720")


def fun():
    messagebox.showinfo("Hello", "Red Button clicked")

def fun2():
    messagebox.showinfo("Hello", "Blue Button clicked")

def fun3():
    messagebox.showinfo("Hello", "Green Button clicked")

def fun4():
    messagebox.showinfo("Hello", "Yellow Button clicked")

c = Canvas(top, bg="pink", height=720, width=720)

b1 = Button(top, text=" Red  ", command=fun, activeforeground="red", activebackground="pink", pady=10, )

b2 = Button(top, text=" Blue ", command=fun2, activeforeground="blue", activebackground="pink", pady=10)

b3 = Button(top, text="Green",command=fun3, activeforeground="green", activebackground="pink", pady=10)

b4 = Button(top, text="Yellow",command=fun4, activeforeground="yellow", activebackground="pink", pady=10)


b1.place(x=10,y=10)

b2.place(x=60,y=10)

b3.place(x=110,y=10)

b4.place(x=160,y=10)

checkvar1 = IntVar()

checkvar2 = IntVar()

checkvar3 = IntVar()

chkbtn1 = Checkbutton(top, text="C", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10)

chkbtn2 = Checkbutton(top, text="C++", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)

chkbtn3 = Checkbutton(top, text="Java", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)

chkbtn1.place(x=10,y=70)

chkbtn2.place(x=10,y=120)

chkbtn3.place(x=10,y=170)

c.pack()

top.mainloop()