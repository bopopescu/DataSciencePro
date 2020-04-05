from dbConn import databasefunctions
print("Type 'add' for adding data in table")
print("Type 'update' for updating in database")
print("Type 'delete' for deleting in database")
print("Type 'create' for creating table in database")
print("Type 'select' for showing table data in database")
print("Type 'selectfletter' for showing table data by first letter in database")
a=input("Enter what u want to do: ")
if(a=="create"):
      b=input("Enter table name u want to create: ")
      databasefunctions.createtable(b)


elif(a=="add"):
      b = input("Enter table name in which u want to add data: ")
      databasefunctions.add(b)

elif(a=="update"):
      b = input("Enter table name in which u want to update data: ")
      databasefunctions.update(b)

elif(a=="delete"):
      b = input("Enter table name in which u want to delete data: ")
      databasefunctions.delete(b)

elif(a=="select"):
      b = input("Enter table name in which u want to select data: ")
      databasefunctions.select(b)

elif(a=="selectfletter"):
      b = input("Enter table name in which u want to select data: ")
      databasefunctions.selectfletter(b)

else:
      print("wrong Input")