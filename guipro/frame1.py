from tkinter import *

top = Tk()
top.geometry("1520x1080")
frame = Frame(top)
frame.pack()

leftframe = Frame(top)
leftframe.pack(side=LEFT)

rightframe = Frame(top)
rightframe.pack(side=RIGHT)
c = Canvas(leftframe, bg="yellow", height=720, width=720)
c1 = Canvas(rightframe, bg="orange", height=720, width=720)
c.pack(side=LEFT)
c1.pack(side=RIGHT)
btn1 = Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT)

btn2 = Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=RIGHT)

btn3 = Button(rightframe, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)

btn4 = Button(leftframe, text="Modify", fg="black", activebackground="white")
btn4.pack(side=RIGHT)

top.mainloop()