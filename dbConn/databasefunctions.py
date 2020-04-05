import mysql.connector
def createtable(x):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()

    a=input("Enter first column and its type and size in format(columnname Type(size):  ")
    t= input("Enter first column and its type and size in format(columnname Type(size):  ")
    sql = "CREATE TABLE " + x + "( " + a + " , " +t+")"

    print(sql)
    mycursor.execute(sql)
    print("Created successfully")

def delete(d):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
    )

    mycursor = mydb.cursor()
    i=input("What u want to delete: ")
    val=input("type "+i+" value: ")

    sql = "DELETE FROM "+d + " WHERE "+i + " = '" + val+"'"
    print(sql)

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def add(c):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()
    x=input("Enter first column: ")
    y=input("Enter second Column: ")

    sql = "INSERT INTO "+c+ " ("+x+" , "+y+" ) VALUES (%s, %s)"
    r=input("Enter the "+x+" : ")
    t=input("Enter the "+y+" : ")
    val = (r, t)
    mycursor.execute(sql, val)
    print(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def update(b):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()
    s=input("Enter what you want to update: ")
    old=input("Type old value: ")
    new=input("Type New value: ")
    sql = "UPDATE " +b+ " SET "+ s+ " = '"+new+ "' WHERE "+ s+ " = '"+ old+"'"
    print(sql)
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

def select(e):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()
    s=input("Enter what u want to select: ")
    mycursor.execute("SELECT "+s+" FROM "+e)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def selectfletter(f):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase2"
    )

    mycursor = mydb.cursor()
    s=input("what you want to show: ")
    d=input("Type first letter: ")
    sql="SELECT "+s+" FROM "+f+" WHERE "+s+" REGEXP '^["+d+"]'"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
