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


