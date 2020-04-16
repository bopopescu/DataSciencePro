import numpy
a = numpy.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
print(a)
print(numpy.percentile([1,4,5,6],50))
print(numpy.percentile(a,50,0))
print(numpy.percentile(a,0,))
print(a)
print("\nMedian of array along axis 0:",numpy.median(a,0))
print("Mean of array along axis 0:",numpy.mean(a,0))
print("Average of array along axis 1:",numpy.average(a,1))

for i in range(0,101):

    print(numpy.percentile([1, 4, 5, 6], i),end=" , ")