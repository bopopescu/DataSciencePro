import numpy

a = numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("Each item contains",a.itemsize,"bytes")
print(a[1,2])
print(type(a))
print("Array Size:",a.size)
print("Shape:",a.shape)
print(a.reshape(3,4))
print(a)
c=a*a
b=numpy.linspace(1,10,12)
print(b)
print(b.reshape(3,4))
x=numpy.asarray(b,dtype=int,order='F')
print(x.reshape(3,4))
print(b[1]-b[0])
print("Arrays vertically concatenated\n",numpy.vstack((a,c)));
print("Arrays horizontally concatenated\n",numpy.hstack((a,c)))
d=numpy.dtype([('salary',numpy.float)])
arr = numpy.array([(10000.12 ),(20000.50 ),(1234.5)],dtype=d)
print(arr['salary'][1])
print(type(arr))

