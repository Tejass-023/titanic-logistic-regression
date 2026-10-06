import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

print("class distribution (species count)")
#print(df("species").value_counts())

print("statical report of dataset :")
print(df.describe())


##########################################################
#
# step 3 : Decide Independant and Dependant  Variables
#
########################################################


print(Border)
print("step 3 : Decide Independant and Dependant  Variables")
print(Border)

#x : Indepndant Variable / features
#Y : Dependant Variable ? Labels

feature_cols = [
    'sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)'
]

X = df[feature_cols]
Y = df["species"]

print("X shape :",X.shape)
print("Y shape  :",Y.shape)




##########################################################
#
# step 4 : Vizulisation of dataset
#
########################################################

print(Border)
print("step 4 : Vizulisation of dataset")
print(Border)

plt.fiqure(figsize= (7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp ]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label=sp)
    
plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length(cm)")
plt.ylabel("petal width(cm)")

plt.legend()
plt.grid()
plt.show()

