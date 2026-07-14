import pandas as pd
from sympy import true , false
# print("Pandas version:", pd.__version__)


data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
        'numbers': [1, 2, 3, 4,],}
# print(type(data))


# series = pd.Series( index=data['Age'], data=data['Name'])
# print(series)
# # print(series.loc[40])

# # series.loc[40] = 'Eve'

# # print(series.loc[40])

# # print(series)

# print(series.iloc[1])

# print(series[series.index > 30])
df = pd.DataFrame(index=data['numbers'], data=data)
df = df.drop(columns=['numbers'])
# print(df)
new_row = pd.DataFrame({'Name': ['Eve'], 'Age': [28], 'City': ['San Francisco'], 'numbers': [5]})
df = pd.concat([df, new_row ], ignore_index=true)
print(df)

