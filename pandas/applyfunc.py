import pandas as pd

bikes = {'COMPANY': ['APPLE', 'META', 'SAMSUNG','ASUS']
          ,'EMP' : ['EMP1', 'EMP2','EMP3','EMP4'],
            'SALARY': [20,12,13,12] }

DF = pd.DataFrame(bikes)

def salaries(x):
    return x*1000

DF["SALARY"]= DF["SALARY"].apply(salaries)
print(DF)
