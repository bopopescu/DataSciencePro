x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))
print("Descending Order:")
if x > y and x > z:
            if y > z:
                print(x, " " ,y , " " , z)
            else:
                print(x , " " , z , " " , y)

elif y > x and y > z:
            if x > z:
                print(y , " " ,x , " " ,z)
            else:
                print(y , " " , z , " " , x)

elif z > x and z > y:
    if x > y:
        print(z, " ", x, " ", y)
    else:
        print(z, " ", y, " ", x)

else:
    print("All are Equal")