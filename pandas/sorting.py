import pandas as pd

bikes = {'COMPANY': ['APPLE', 'META', 'SAMSUNG','ASUS']
          ,'EMP' : ['EMP1', 'EMP2','EMP3','EMP4'],
            'SALARY': [20,12,13,12] }

df = pd.DataFrame(bikes)
# df.sort_values("SALARY" , ascending=False, inplace= True)
# print(df)
print(pd.DataFrame(pd.DataFrame(bikes)["SALARY"].unique()))
print(pd.DataFrame(df["SALARY"].unique()))