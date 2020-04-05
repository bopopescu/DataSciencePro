import numpy as np
arr = np.empty((3, 3), dtype=int)
print(arr[2][1])
i = b'hello world'
print(type(i))

a = np.frombuffer(i, dtype="S1")
print(a)
print(a[3])
b=np.arange(0, 18, 1.5, float)
print(b)
print(b.reshape(3, 4))
arr2 = np.logspace(10, 20, num = 5,base = 2, endpoint = True)
print("The array over the given range is ",arr2)
