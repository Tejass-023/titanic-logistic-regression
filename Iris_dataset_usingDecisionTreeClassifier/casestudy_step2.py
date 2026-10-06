import pandas as pd

Border = "-"*30
#########################################
#
# step 1 : Load the datset
#
#########################################

print(Border)
print("Step 1 : Load the datset")
print(Border)

Datapath = r"C:\Users\tejas\Desktop\python\machine laearning\iris.csv"

df = pd.read_csv(Datapath)

print("datset loaded succesfully")
print("initial enteries from datset are:")
print(df.head())

#########################################
#
# step 2 : Data Analysis (EDA)
#
#########################################

print(Border)
print("step 2 : Data anaylisi (EDA)")
print(Border)

print("Shape of Dataset :" , df.shape)
print("colums names :",list(df.columns))

print("missing values per column :")
print(df.isnull().sum())

print("class distribution (spicies count)")
print(df("species").value_counts())

print("statical report of dataset :")
print(df.describe())