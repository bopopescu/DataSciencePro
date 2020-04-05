import numpy as np

a = np.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])

print("\nPrinting the array:\n")

print(a)
print(a*3)

print("\nPrinting the transpose of the array:\n")
at = a.T

print(at)

print("\nIterating over the transposed array\n")

for x in np.nditer(at):
    print(x, end=' ')

print("\nSorting the transposed array in C-style:\n")

c = at.copy(order='C')

print(c)

print("\nIterating over the C-style array:\n")
for x in np.nditer(c):
    print(x, end=' ')

d = at.copy(order='F')
print()
print(d)
print("Iterating over the F-style array:\n")
for x in np.nditer(d):
    print(x, end=' ')

print("\nptp value along axis 1:", np.ptp(a, 1))

print("ptp value along axis 0:", np.ptp(a, 0))