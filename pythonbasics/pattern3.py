print("Triangle")
n=int(input("Enter the rows: "))
v = 2 * n - 2
for i in range(0, n):
    for j in range(0, v):
        print(end=" ")
    v = v - 2
    for j in range(0, i + 1):
        print(" * ", end=" ")
    print("\r")