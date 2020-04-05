import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase2")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)