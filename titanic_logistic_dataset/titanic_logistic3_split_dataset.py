import pandas as pd
import numpy as np
import joblib as jb

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix


# step 1 : Load the data


#-------------------------------------------------------------------------------------
#
#   Function Name : Load Data 
#   Description   : Load the data from csv
#   Input         : Name of Csv file
#   Output        : Data frame
#   Author        : Tejas Anil More
#   Date          : 16-08-2026
#
#-----------------------------------------------------------------------------------------

def loaddata(filename):
    df = pd.read_csv(filename)
    print(df.head())
    return df



#-------------------------------------------------------------------------------------
#
#   Function Name : preprocess data
#   Description   : It performs data anlysis
#   Input         : dataframe
#   Output        : updated Data frame
#   Author        : Tejas Anil More
#   Date          : 16-08-2026
#
#-----------------------------------------------------------------------------------------

def preprocessdata(df):
    df = df.drop(["Passengerid" , "zero",], errors = "ignore")
    

#Handle missing values
    df ["Age"] = df["Age"].fillna(df["Age"].median())

    df ["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df ["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    print(df.head())
    
    
    df = pd.get_dummies(         #get dummis works like a one hot encoding
        df,
        columns = ["Embarked"],
        drop_first =  True,
        dtype = int,
    )
    return df

#-------------------------------------------------------------------------------------
#
#   Function Name : splits the data
#   Description   : It performs spliting of data
#   Input         : dataframe
#   Output        : Four subsets of training and testing
#   Author        : Tejas Anil More
#   Date          : 16-08-2026
#
#-----------------------------------------------------------------------------------------

def SplitData(df):
    X = df.drop("Survived" , axis = 1)
    Y = df["Survived"]
    
    X_train ,X_test , Y_train ,Y_test = train_test_split(X , Y , test_size= 0.2 , random_state= 42)
    
    return X_train ,X_test , Y_train ,Y_test

#-------------------------------------------------------------------------------------
#
#   Function Name : main
#   Description   : Entry point function
#   Input         : none
#   Output        : none
#   Author        : Tejas Anil More
#   Date          : 16-08-2026
#
#-----------------------------------------------------------------------------------------



    
def main():
    #step 1 :
    df = loaddata("C:/Users/tejas/Desktop/machine laearning/titanic_logistic_dataset/MarvellousTitanicDataset.csv")
    
    #step 2:
    df = preprocessdata(df)
    
    #step 3:
    def SplitData(df):
        
    
if __name__ == "__main__":
    main()
    