principle=float(input("Enter the integer Principal: "))
rate=float(input("Enter the integer Rate: "))
time=float(input("Enter the integer Time: "))
simpleInterest= (principle*rate*time)/100
ci=(principle*(1+(rate/100))**time)
print("Simple Interest: ",simpleInterest)
print("Compound Interest : ",ci)


firstname=input("Enter Fisrt name: ")
lname = input("Enter  LastName: ")
print(" welcome "+firstname+" "+lname)
