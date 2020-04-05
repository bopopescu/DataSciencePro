import pandas as pd
import numpy as np
emp = ['Parker', 'John', 'Smith', 'William']
id = [102, 107, 109, 114]
emp_series = pd.Series(emp)
id_series = pd.Series(id)
frame = { 'Emp': emp_series, 'ID': id_series }
result = pd.DataFrame(frame)
print(result)
s = pd.Series(["a", "b", "c"],  name="vals")
print(s.to_frame())
print(pd.unique(id_series))
print(pd.unique(pd.Series([pd.Timestamp('20160101')])))
index = pd.Index([2, 1, 1, np.nan, 3])
print(index.value_counts() )
a = pd.Series([2, 1, 1, np.nan, 3])
print(a.value_counts(normalize=True))
print(a)
print(a.value_counts(bins=2)  )
print(a.value_counts(dropna=False)  )