import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import  mean_squared_error , r2_score





#------------------------------------------------------------------------
# Step 1 : Load the data
#--------------------------------------------------------------------------

df = pd.read_csv("C:/Users/tejas/Desktop/machine laearning/california_dataset/california_housing.csv")

print("shape of dataset : " ,df.shape)
print("first dew records : " , df.head())



#------------------------------------------------------------------------
# Step 2 : sepreate features and labels 
#--------------------------------------------------------------------------

X = df.drop("target" , axis = 1)
Y = df["target"]

print("shape of X :" ,X.shape)
print("shpe of Y  :", Y.shape)  


#------------------------------------------------------------------------
# Step 3 : split the dataset for the training and testing 
#--------------------------------------------------------------------------


X_train , X_test , Y_train , Y_test =  train_test_split(X,Y,random_state=42,test_size=0.2)

#------------------------------------------------------------------------
# Step 4.1 : crate the base model
#--------------------------------------------------------------------------

base_model = DecisionTreeRegressor(random_state=42)

#------------------------------------------------------------------------
# Step 4.2 : Create the model 
#--------------------------------------------------------------------------


model = BaggingRegressor(
    estimator= base_model,
    n_estimators=10,
    random_state=42
    
    
)




#------------------------------------------------------------------------
# Step 5 : Train the model 
#--------------------------------------------------------------------------

model = model.fit(X_train,Y_train)



#------------------------------------------------------------------------
# Step 6 : Test the model 
#--------------------------------------------------------------------------

Y_pred = model.predict(X_test)

#------------------------------------------------------------------------
# Step 7 : evaluate the model  
#--------------------------------------------------------------------------


print("MSE : " , mean_squared_error( Y_test , Y_pred))
print("R2" , r2_score(Y_test , Y_pred) )