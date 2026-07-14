import pandas as pd
import numpy as np

baddies = {'Names' : ['Angelina Jolie', 'Ana de Armas', 'Scarlett Johansson', 'Gal Gadot', 'Margot Robbie'],
            'Currently' : ['Mine', 'Mine', 'Mine', 'Mine', 'Mine'],
            'Age' : [48, 35, 38, 37, 32],
            'Her ex' : [np.nan, np.nan, np.nan, np.nan, np.nan]
            }

df = pd.DataFrame(baddies)

# df2 = df.drop('Her ex', axis=1, inplace=True) #inplace=True modifies the original dataframe and returns None
# print(df)
# print(df2) #returns None because inplace=True, it modifies the original dataframe and returns None

df3 = df.drop(0, axis=0, inplace=False) #inplace=False returns a new dataframe and does not modify the original dataframe
print(df3)