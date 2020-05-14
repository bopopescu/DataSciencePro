import random
a=random.randint(1,100)
print(a)
print(random.randrange(9,13,3))

print(random.random())
print(random.triangular(20, 60, 0))
mylist = ["Spade", "Hearts", "Diamond","Club"]
mylist2=["Ace","two","three","Four","five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
b= random.choice(mylist)
c= random.choice(mylist2)
d= random.choice(mylist)
e= random.choice(mylist2)
print(" First card is : ",c," of ",b)
print(" Second card is : ",e," of ",d)

random.shuffle(mylist2)

print(mylist2)