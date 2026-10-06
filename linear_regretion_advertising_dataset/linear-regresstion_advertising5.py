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
   print("step 3 : remove  missing values ")
   print(border)  
   
   print(border)
   print(df.describe())
   print(border)
    
    
    
   

  
   
   
   #step 5 : correlation
   
   
   
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
   
    


def main():
    MarvellousRegression("C:/Users/tejas/Desktop/machine laearning/linear_regretion_advertising_dataset/Advertising.csv")





if __name__ == "__main__":
    main()
