x=int(input("Enter the 1st number: "))
y=int(input("Enter the 2nd number: "))
rng=int(input("Enter the range: "))
n=0
print("These are the numbers which are not divisible by",x," and ",y," : ")
while(n<=rng) :
    n+=1
    if n == rng:
        break
    if n%x==0 or n%y==0 :
        continue

    print(n,end=" ")






