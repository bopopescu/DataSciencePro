x = lambda a, b: a+b

print(x(2, 3))

def table(n):
    return lambda a: n*a

y = table(10)

for i in range(1,11):
    print(y(i))
