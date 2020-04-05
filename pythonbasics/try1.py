x=int(input("Enter the number: "))
y=int(input("Enter the second number: "))

try :
    c=x/y
    print(c)
except :
    print("Exception")

else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")
if y <= 0:
  raise Exception("Sorry, no numbers below zero")