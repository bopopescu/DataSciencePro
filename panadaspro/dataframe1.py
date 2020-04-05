import pandas as pd
df2={"ajay":
         {
             "name":"ajay",
             "Branch":"It",
             "Batch": 2016
         }
     }
df = pd.DataFrame(df2)
print (df)

print(df2)
info = {'ID' :[101, 102, 103],'Department' :['B.Sc','B.Tech','M.Tech',]}
df3 = pd.DataFrame(info)
print (df3)
info2 = {'one': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
        'two': pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}

d1 = pd.DataFrame(info2
                  )
print(d1)
d1['three']=pd.Series([20,40,60],index=['a','b','c'])
print (d1)
print(d1.loc['b'])
print(d1.iloc[2])
print(d1[1:4])

d = pd.DataFrame([[7, 8], [9, 10]], columns = ['x','y'])
d2 = pd.DataFrame([[11, 12], [13, 14]], columns = ['x','y'])
d = d.append(d2)
print (d)
a_info = pd.DataFrame([[4, 5], [6, 7]], columns=['x', 'y'])
b_info = pd.DataFrame([[8, 9], [10, 11]], columns=['x', 'y'])

a_info = a_info.append(b_info)


a_info = a_info.drop(0)
print(a_info)