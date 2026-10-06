import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


def MarvellousRegression(Datapath):
    
   border = "-" * 40
   
   #step 1 : load the data
   
   print(border)
   print("step 1 : load the data")
   print(border)
   
   
   df = pd.read_csv(Datapath)
   print(df.head())
   
   
   
   
   #step 2 : remove unwanytedd columns 
   
   
   print(border)
   print("step 2 : remove unwanytedd columns ")
   print(border)
   
   if "unnamed : 0" in df.columns:
       df = df.drop(columns = ["unmaned : 0"])
       
       print(df.head())
       
       
       
    #step 3 : remove missing values
    
    
       
   print(border)
   print("step 3 : remove  missing values ")
   print(border)
   
   print(border)
   print(df.isnull().sum())
   print(border)
    
   # step 4 ; stastical summary
   
   
   print(border)
   print("step 4 : stastical summary ")
   print(border)  
   
   print(border)
   print(df.describe())
   print(border)
     
   
   #step 5 : correlation
   
   
   print(border)
   print("step 5 : correlation")
   print(border)   
   
   
   print(border)
   print(df.corr())
   print(border)
   
   
   #step 6 : seprate dependant and independant variable 
   
   
   print(border)
   print("step 6 : seprate dependant and independant variable")
   print(border)
    
   X = df[["TV","radio","newspaper"]]
   Y = df["sales"]
   
   print("independant variable :" ,X)
   print("depndant variable : " , Y)
   
   
   #step 7 : split the dataset
   
   
   print(border)
   print("step 7 : split the dataset")
   print(border)
   
   X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2 , random_state=42)
   
   print("training data : " , X_train.shape)
   print("Testing data : " , X_test.shape)
   
   
   #step 8 : create and train the model 
   
   print(border)
   print("step 8 : create and train the model")
   print(border)  
   
   model = LinearRegression()
   model = model.fit(X_train , Y_train)
   
   print("model trainied successfully.....")
   
   #step 9 : test the model 
   
   print(border)
   print("step 9 :; test the model :")
   print(border)
   
   Y_pred = model.predict(X_test)
   
   print(Y_pred[:5])    #[:5] -> it means pahile 5 
   
   
   print("expected answers : ")
   print(Y_test[:3])
   
   print("pridected answers : ")
   print(Y_pred[:3])

def main():
    MarvellousRegression("C:/Users/tejas/Desktop/machine laearning/linear_regretion_advertising_dataset/Advertising.csv")

    



if __name__ == "__main__":
    main()
