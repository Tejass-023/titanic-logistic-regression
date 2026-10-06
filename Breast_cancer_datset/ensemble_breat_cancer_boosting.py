import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

from sklearn.ensemble import AdaBoostClassifier 



#-------------------------------------------------------------
# Satep 1 : Load the dataset
#-------------------------------------------------------------

df = pd.read_csv("C:/Users/tejas/Desktop/machine laearning/Breast_cancer_datset/breast_cancer.csv")

print("shape of dataset : " , df.shape)

print("First few records : ")
print(df.head())

#--------------------------------------------------------------
#  step 2 : Seprate the features and labels
#---------------------------------------------------------------

X = df.drop("target" , axis = 1)
Y = df["target"]

print("X shape : " , X.shape)
print("Y shape :" , Y.shape)




#--------------------------------------------------------------
#  step 3 : Split the dataset from traing and testing
#---------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

 
 

 
#--------------------------------------------------------------
#  step 4 : scale the data
#---------------------------------------------------------------


scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#--------------------------------------------------------------
#  step 5 : Create the boosting model
#---------------------------------------------------------------

model = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1.0,
    random_state=42
    
)


#--------------------------------------------------------------
#  step 6 : Train the model
#---------------------------------------------------------------


model = model.fit(X_train,Y_train)

#--------------------------------------------------------------
#  step 7 : test the model
#---------------------------------------------------------------

Y_pred = model.predict(X_test)


#--------------------------------------------------------------
#  step 8 : Evaluate the model
#---------------------------------------------------------------

print ("Accurecy : " , accuracy_score(Y_test,Y_pred))

print("confustion matrix : " , confusion_matrix(Y_test,Y_pred))


