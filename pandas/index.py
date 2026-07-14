import pandas as pd

dccomics = pd.read_csv(r"C:\Users\kartik tanvar\Downloads\dc-wikia-data.csv")
# df = pd.DataFrame(dccomics)

df1 = dccomics.head(5)[["name", "SEX" , "YEAR" , "HAIR"]]
print(df1)

df1["hero no."] = [1,2,3,4,5]

df1.set_index("hero no." , inplace = True)
print(df1)

df1.reset_index(inplace = True)
print(df1)

df1.drop("hero no.", axis = 1, inplace = True)
print(df1)


