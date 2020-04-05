def table(x,i=1):
    print(x*i)
    if i!=10:
        table(x,i+1)


x=int(input("Enter the number: "))
print(table(x))