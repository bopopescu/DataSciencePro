import pandas as pd
import numpy as np
info = {'x' : 0., 'y' : 1., 'z' : 2.}
a = pd.Series(info)
print (a)
into=["ajay","chopra",1,"chopra2",2,"chand"]
b=pd.Series(into)
print(b)
x = pd.Series([4,2,6,9], index=[3, 6, 2, 8])
print (x[6])
print(x.index)
print(x.values)
a2=pd.Series(data=[1,2,3,4])
b2=pd.Series(data=[4.9,8.2,5.6],   index=['x','y','z'])
print(a2.dtype)
print(b2.dtype)
print(b2.size)
print(b.shape)
a3 = pd.Series(['Java', 'C', 'C++', np.nan])
a3.map({'Java': 'Core'})
a3.map('I like {}'.format)
# a3.map('I like {}'.format, na_action='ignore')
print(a2.std())
inr = {
    'Name':['Parker','Smith','John','William'],
   'sub1_Marks':[52,38,42,37],
   'sub2_Marks':[41,35,29,36]}
data = pd.DataFrame(inr)
print(data)
print(data.std())