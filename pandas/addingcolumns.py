import pandas as pd
import numpy as np

horses = {'Name': ['Secretariat', 'Seabiscuit', 'Black Caviar', 'Frankel'],
          'Year': [1973, 1933, 2006, 2008],
          'Wins': [16, 33, 25, 14]
          }
df1 = pd.DataFrame(horses)
#method1, using lists
# loses = [3, 4, 2, 1]
# df1['Loses'] = loses
# print(df1)
# #for null values, we can use numpy.nan
# df1['Husband/Wife'] = [np.nan]*len(df1)
# print(df1)

#method2, using insert function
# df1.insert(3, 'Loses', [3, 4, 2, 1])
# print(df1)

#method3, using assign function, it returns a new dataframe, so we need to assign it to a variable
df2 = df1.assign(Loses=[3, 4, 2, 1])
print(df2)
print(df1) #original dataframe remains unchanged




