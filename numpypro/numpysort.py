import numpy as np

a = np.array([[10, 2, 30], [4, 50, 60], [7, 8, 50]])

print("Sorting along the columns:")
print(np.sort(a))

print("Sorting along the rows:")
print(np.sort(a, 0))

data_type = np.dtype([('name', 'S10'), ('marks', int)])

arr = np.array([('Mukesh', 200), ('John', 251)], dtype=data_type)

print("Sorting data ordered by name")

print(np.sort(arr, order='name'))

a2 = np.array(['a', 'b', 'c', 'd', 'e'])

b = np.array([12, 90, 380, 12, 211])

ind = np.lexsort((a2, b))

print("printing indices of sorted data")

print(ind)

print("using the indices to sort the array")

for i in ind:
    print(a2[i], b[i])

c = np.array([[20, 24], [21, 23]])

print(np.where(c > 20))
print(a[2][2])
print(np.where(a > 20))
print(a.nonzero())