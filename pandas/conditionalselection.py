import pandas as pd 

dccomics = pd.read_csv(r"C:\Users\kartik tanvar\Downloads\dc-wikia-data.csv")
df = pd.DataFrame(dccomics)



# print(df == 2013) #dataframe of boolean values
print(df[df == 2013]) #dataframe of 2013 values and NaN values
# print(df[df['YEAR'] == 2013]) #dataframe of rows where year is 2013
# print(df[df['YEAR'] == 2013]['SEX']) #series
# print(df[df['YEAR'] == 2013][['SEX', 'ALIVE']]) #dataframe where year is 2013
# print(df[df['YEAR'] >= 1980][['SEX', 'ALIVE']].to_string()) #dataframe where year is greater than or equal to 1980

print(df[(df['SEX'] == 'Male Characters') & (df['YEAR'] == 2013)]) #multiple conditions