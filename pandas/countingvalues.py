import pandas as pd


dccomics = pd.read_csv(r"C:\Users\kartik tanvar\Downloads\dc-wikia-data.csv")
#a = dccomics['page_id'].value_counts()
#print(a.head(10))
# print(dccomics.columns)
b = dccomics['SEX'].value_counts(dropna=False)
print(b) 
# c = dccomics['ALIVE'].value_counts(normalize=True, dropna=False)
# print(c)
# d = dccomics['YEAR'].value_counts(normalize=True, dropna=False)
# print(d.to_string())
# v = dccomics.groupby('SEX').size()
# print(v)

#we can use unique() function to get unique values and it returnes an array
#like
print(dccomics["name"].unique())#array
print(pd.DataFrame(dccomics["name"].unique())) #dataframe


