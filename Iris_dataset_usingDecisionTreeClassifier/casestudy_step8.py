import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier


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

plt.figure(figsize= (7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp ]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label=sp)
    
plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length(cm)")
plt.ylabel("petal width(cm)")

plt.legend()
plt.grid()
plt.show()

##########################################################
#
# step 5 : split the datset for testing and trainig 
#
########################################################

print(Border)
print("step 5 : split the datset for testing and trainig")
print(Border)

X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.5, random_state = 42)

print("datset splitting activity done")

print("X_train :" , X_train.shape)
print("X_test :" , X_test.shape)

print("Y_train :" , Y_train.shape)
print("Y_test :" , Y_test.shape)


##########################################################
#
# step 6 : Build the model
#
########################################################


print(Border)
print("step 6 : Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth = 5)

print("model gets created successfully ")


##########################################################
#
# step 7 : Train the model
#
########################################################

print(Border)
print("step 7 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("model trains succeesfully")


##########################################################
#
# step 8 : test the model
#
########################################################

print(Border)
print("step 8 : Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("model testing done..")
print("expected answers : ")
print(Y_test)

print("expected answers :")
print(Y_pred)