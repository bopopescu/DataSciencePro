a=int(input("Enter the number of rows : "))
#floyds triangle
n=1
for i in range(a):
    for j in range(0,i+1):

        print(n,end=" ")
        n=n+1

    print()

#Number traingle
for i in range(a):
    for j in range(i+1):

        print(i+1,end=" ")


    print()

# second Number triangle
for i in range(a):
    for j in range(i+1):

        print(j+1,end=" ")


    print()

#Alphabatic pattern
for i in range (65,65+a):
    # inner loop
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()

#Alphabatic Patterns
for i in range (65,a+65):

    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()