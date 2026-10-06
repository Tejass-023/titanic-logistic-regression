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
       
    #step 2 : remove missing values
       
   print(border)
   print("step 3 : remove  missing values ")
   print(border)
    
   # step 3 ; stastical summary
   
   
   print(df.describe())
    
    
    
    

   print(border)
   print(df.isnull().sum())
   print(border)
    
    
    


def main():
    MarvellousRegression("C:/Users/tejas/Desktop/machine laearning/linear_regretion_advertising_dataset/Advertising.csv")





if __name__ == "__main__":
    main()
