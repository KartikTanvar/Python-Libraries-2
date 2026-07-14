import pandas as pd
import numpy as np

baddies = {'Names' : ['Angelina Jolie', 'Ana de Armas', 'Scarlett Johansson', 'Gal Gadot', 'Margot Robbie'],
            'Currently' : ['Mine', 'Mine', 'Mine', 'Mine', 'Mine'],
            'Age' : [48, 35, 38, 37, 32],
            'Her ex' : [np.nan, np.nan, np.nan, np.nan, np.nan]
            }

df = pd.DataFrame(baddies)
print(df)


#just use loc and iloc to grab rows
print(df.loc[0])  # grab the first row
print(df.loc[0, 'Names'])  # returns angelina jolie(point)
print(df.loc[[0, 1], ['Names', 'Currently']])  # a subset(in the form of a dataframe)
#we can also use iloc to grab rows by index
