n=int(input("Enter the number of rows: "))
for i in range(0,n+1):
    for j in range (n,i,-1):
       print( end=" ")

    for k in range(0,i):
        print("*" ,end=" ")

    for j in range (2*n,i*2,-1):
       print( end=" ")

    for k in range(0,i):
        print("*" ,end=" ")
    print()
