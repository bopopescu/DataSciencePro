n=int(input("Enter the num of rows you want to print : "))
#Right angle Triangle
print("Right angle triangle")
for i in range(0,n) :
    for x in range(0,i+1):
        print("* " , end=" ")
    print("\r")
#ulta Right angle Triangle
print("Ulta Right angle triangle")
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")
#Triangle
print("Triangle")
v = 2 * n - 2
for i in range(0, n):
    for j in range(0, v):
        print(end=" ")
    v = v - 2
    for j in range(0, i + 1):
        print(" * ", end=" ")
    print("\r")