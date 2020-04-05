from tkinter import *
import mysql.connector
from tkinter import messagebox


def adddata2(root,sr1,topic1,link1,date1):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO  users ( Sr , topic , link , date ) VALUES ( %s , %s , %s , %s )"
    val = (sr1.get(),topic1.get(),link1.get(),date1.get())

    mycursor.execute(sql, val)

    mydb.commit()
    if mycursor.rowcount:
        messagebox.showinfo("Congratx",  "record inserted.")

def select(root):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT *  FROM users")
    myresult = mycursor.fetchall()
    return myresult

def update2(root,updation,old,new):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()
    sql = "UPDATE users SET " + updation.get() + " = '" + new.get() + "' WHERE " + updation.get() + " = '" + old.get() + "'"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    if mycursor.rowcount:
        messagebox.showinfo("Congratx", "record updated.")


def delete2(root,i,val):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()
    sql = "DELETE FROM users  WHERE " + i.get() + " = '" + val.get() + "'"
    mycursor.execute(sql)

    mydb.commit()
    if mycursor.rowcount:
        messagebox.showinfo("Congratx", "record deleted.")







