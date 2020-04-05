import numpy as np

a = 10
b = 12

print("binary representation of a:", bin(a))
print("binary representation of b:", bin(b))
print("Bitwise-and of a and b: ", np.bitwise_and(a, b))
print("Bitwise-or of a and b: ",np.bitwise_or(a,b))
arr = np.array([20], dtype=np.uint8)
print("Binary representation:", np.binary_repr(20, 8))

print(np.invert(arr))

print("Binary representation: ", np.binary_repr(235, 8))
print("left shift of 20 by 3 bits",np.left_shift(20, 3))

print("left shift of 20 by 3 bits",np.right_shift(20, 3))
print(np.char.center("Javatpoint", 20, '*'))
arr2 = np.array([0, 30,45, 60, 90, 120, 150, 180])
print("\nThe sin value of the angles",end = " ")
print(np.sin(arr2 * np.pi/180))
print("\nThe cosine value of the angles",end = " ")
print(np.cos(arr2 * np.pi/180))
print("\nThe tangent value of the angles",end = " ")
print(np.tan(arr2 * np.pi/180))
arr3 = np.array([12.202, 90.23120, 123.020, 23.202])

print(np.around(arr3, -1))
print(np.around(arr3, 2))
print(np.floor(arr3))
print(np.ceil(arr3))