import mysql.connector
from tkinter import *
from tkinter import messagebox
from guipro import tkinter5



def login2():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )
    mycursor = mydb.cursor()
    sql= "SELECT * FROM admin WHERE username = '"+name.get()+"' and password = '"+pswd.get()+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult:
        messagebox.showinfo("Congratx","Login Successfully")
        top.withdraw()
        operations()

    else:
        messagebox.showinfo("Error","Something WENT wrong")

def operations():
    bottom = Toplevel(top)

    bottom.title("Operations")

    bottom.geometry("400x400")
    b1 = Button(bottom, text=" Add data  ", command=lambda :adddata(bottom), activeforeground="red", activebackground="pink", pady=10, )

    b2 = Button(bottom, text=" Show data ", command=lambda :showlist(bottom), activeforeground="blue", activebackground="pink", pady=10)

    b3 = Button(bottom, text="Update data", command=lambda:updatedate(bottom), activeforeground="green", activebackground="pink", pady=10)

    b4 = Button(bottom, text="Delete data", command=lambda :deleterow(bottom), activeforeground="yellow", activebackground="pink", pady=10)

    b1.place(x=10, y=10)

    b2.place(x=10, y=60)

    b3.place(x=10, y=110)

    b4.place(x=10, y=160)

    bottom.mainloop()

def adddata(bottom):

    add=Toplevel(bottom)
    bottom.withdraw()
    add.title("Add Data")
    add.geometry("400x400")

    sr1 = StringVar()
    topic1 = StringVar()
    link1 = StringVar()
    date1 = StringVar()

    sr = Label(add, text="Sr")

    topic= Label(add, text="Topic")

    link = Label(add, text="Link")

    date = Label(add, text="Date")

    e1sr = Entry(add, textvariable=sr1, width=20)

    e2topic = Entry(add, textvariable=topic1, width=20)

    e3link = Entry(add, textvariable=link1, width=20)

    e4date = Entry(add, textvariable=date1, width=20)

    sr.place(x=30, y=50)
    topic.place(x=30, y=90)
    link.place(x=30, y=130)
    date.place(x=30, y=170)
    e1sr.place(x=100, y=50)
    e2topic.place(x=100, y=90)
    e3link.place(x=100, y=130)
    e4date.place(x=100, y=170)
    b1 = Button(add, text=" Add data  ", command=lambda: tkinter5.adddata2(add,sr1,topic1,link1,date1), activeforeground="red", activebackground="pink", pady=10)
    b2 = Button(add, text=" Back  ", command=lambda: back(add), activeforeground="red", activebackground="pink", pady=10)
    b1.place(x=100,y=210)
    b2.place(x=200,y=210)
    add.mainloop()


def showlist(bottom):
    select=Toplevel(bottom)
    select.title("Show List")
    select.geometry("720x720")
    bottom.withdraw()
    list2 = Label(select, text="List")
    list2.place(x=50, y=10)
    listBox= Text(select,width = 140)
    listBox.place(x=50, y=50)
    z=tkinter5.select(bottom)
    listBox.insert(END, "sr | Topic\t\t\t|Link\t\t\t\t\t |Date\n")
    listBox.insert(END, "-------------------------------------------------------------------------------------------------")
    listBox.insert(END, "\n")
    for i in range(len(z)):
        # listBox.insert(END, (i + 1))
        # listBox.insert(END, "\t |")
        listBox.insert(END, z[i][0])
        listBox.insert(END, "  |  ")
        listBox.insert(END, z[i][1])
        listBox.insert(END, "\t|")
        listBox.insert(END, z[i][2])
        listBox.insert(END, "\t\t\t|")
        listBox.insert(END, z[i][3])
        listBox.insert(END, "\n")

    select.mainloop()


def updatedate(bottom):
    update=Toplevel(bottom)
    update.title("Update")
    update.geometry("720x720")
    bottom.withdraw()
    update1 = StringVar()
    old1 = StringVar()
    new1 = StringVar()
    updation = Label(update, text="Updation")

    old = Label(update, text="Old Value")


    new = Label(update, text="New Value")

    e1update = Entry(update, textvariable=update1, width=20)

    e2old = Entry(update, textvariable=old1, width=20)

    e3new = Entry(update, textvariable=new1, width=20)

    updation.place(x=30, y=50)
    old.place(x=30, y=90)
    new.place(x=30, y=130)
    e1update.place(x=100, y=50)
    e2old.place(x=100, y=90)
    e3new.place(x=100, y=130)
    b1 = Button(update, text=" Update data  ", command=lambda: tkinter5.update2(update, update1, old1, new1), activeforeground="red", activebackground="pink", pady=10, )
    b1.place(x=100, y=210)
    update.mainloop()


def deleterow(bottom):
    delete=Toplevel(bottom)
    delete.title("Delete")
    delete.geometry("720x720")
    bottom.withdraw()
    deletion2 = StringVar()
    value1   = StringVar()
    deletion = Label(delete, text="Column Name")

    value = Label(delete, text=" Value")
    e1column = Entry(delete, textvariable=deletion2, width=20)

    e2value = Entry(delete, textvariable=value1, width=20)
    deletion.place(x=50, y=50)
    value.place(x=50, y=90)
    e1column.place(x=100, y=50)
    e2value.place(x=100, y=90)
    b1 = Button(delete, text=" Delete data  ", command=lambda: tkinter5.delete2(bottom,deletion2,value1), activeforeground="red", activebackground="pink", pady=10, )
    b1.place(x=100, y=150)
    delete.mainloop()


def back(root1):
    operations()
    root1.destroy()





top = Tk()

name = StringVar()
pswd = StringVar()

top.geometry("400x400")

uname = Label(top, text="Username").place(x=30, y=50)

password = Label(top, text="Password").place(x=30, y=90)

e1 = Entry(top,textvariable=name, width=20).place(x=100, y=50)

e2 = Entry(top,textvariable=pswd, width=20).place(x=100, y=90)

login = Button(top, text="Login", command=login2, activebackground="pink", activeforeground="blue").place(x=100, y=120)

top.mainloop()