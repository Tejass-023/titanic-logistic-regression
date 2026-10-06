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
#   Function Name : Load Data 
#   Description   : Load the data from csv
#   Input         : Name of Csv file
#   Output        : Data frame
#   Author        : Tejas Anil More
#   Date          : 16-08-2026
#
#-----------------------------------------------------------------------------------------
def main():
    loaddata("C:/Users/tejas/Desktop/machine laearning/titanic_logistic_dataset/MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()
    