import queue
x = ["Python", "C", "Android"]
x.append("ajay")
print(x)
print(x)
print(x.pop())
print(x)
print(x.pop())
print(x)
x.insert(1,"C++")
print(x)
L = queue.Queue(maxsize=10)
L.put(9)
L.put(6)
L.put(7)
L.put(4)
# print(L.get())
# print(L.get())
# print(L.get())
# print(L.get())

for i in range(L.maxsize):
    print(L.get(),end=" ")
