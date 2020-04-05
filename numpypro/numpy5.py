import numpy
a = numpy.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
print(numpy.percentile(a,10,1))
print(numpy.percentile(a,10,))
print(a)
print("\nMedian of array along axis 0:",numpy.median(a,0))
print("Mean of array along axis 0:",numpy.mean(a,0))
print("Average of array along axis 1:",numpy.average(a,1))
