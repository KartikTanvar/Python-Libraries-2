import pandas as pd
import numpy as np

baddies = {'Names' : ['Angelina Jolie', 'Ana de Armas', 'Scarlett Johansson', 'Gal Gadot', 'Margot Robbie'],
            'Currently' : ['Mine', 'Mine', 'Mine', 'Mine', 'Mine'],
            'Age' : [48, 35, 38, 37, 32],
            'Her ex' : [1 , np.nan, np.nan, np.nan, np.nan]
            }

df = pd.DataFrame(baddies)

# print(df.dropna(thresh = 2, axis=1))
# df['Her ex'] = df['Her ex'].astype(object)
# df.fillna(value="no one" , inplace = True)
# print(df)

#we can also use maths functions like min max mean etc to fill nan values, for instance

df.fillna(value = df["Age"].mean(), inplace = True)
print(df)
df.fillna(value = df["Her ex"].sum(), inplace = True)
print(df)

