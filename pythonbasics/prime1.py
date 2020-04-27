num=int(input("Enter the number: "))
flag=0
m=num//2
for i in range(2,m+1):
    if(num%i==0):
        print("number is not prime")
        flag=1
        break
if(flag==0):
    print("number is prime")