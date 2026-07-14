import numpy as np 
import pandas as pd

np1 = np.array([[1, 2, 3], [4, 5, 6]])
series1 = pd.DataFrame(data=np1 , index=[1, 2, 3])
print(series1)

