import pandas as pd
from sympy import true 

df = pd.read_csv(r"C:\python\Python Libraries folder\pandas\MARVELDATA.csv")
#print(df[['name', 'ALIVE']].to_string())


#print(df[df['ALIVE'] == 'Deceased Characters'][['name', 'ALIVE']].to_string(index=true))

#print(df.loc[df['name'] == 'Spider-Man (Peter Parker)', ['name', 'ALIVE']].to_string(index=true))

#print(df.iloc[0:3].to_string(index=true))

print(df[df['ALIVE'] == 'Deceased Characters'][['name', 'ALIVE']].to_string(index=true))
