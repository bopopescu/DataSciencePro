from array import array

arr = array('d',[428,54,5453463400,5653.45634,634253425])

print(arr)
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
arr.append(5)
print(arr)
arr.reverse()
print(arr)
