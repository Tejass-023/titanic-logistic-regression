import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def marvellousClassifier(Datapath):

    border = "-" * 40

    # Load dataset
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(Datapath)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)
    
    #clean datase
    
    print(border)
    print("step 2 : clean the dataset")
    print(border)
    
    df.dropna(inplace = True)
    
    print(border)
    print("shape of dataset : " , df.shape)
    
    print("total rows : " , df.shape[0])
    print("total colums : " , df.shape[1])
    
    
    #sepratre the variables 
    
    print(border)
    print("step 3 : seprate independant and depenadt variable ")
    print(border)
    
    X = df.drop(columns = ['Class'])
    Y = df['Class']
    
    print("shape of X : " , X.shape)
    print("shape of Y : " , Y.shape)
    
    
    print(border)
    print("input columns : " , X.columns.tolist())
    print("output columns : class ")
    print(border)


def main():
    marvellousClassifier("C:/Users/tejas/Desktop/machine laearning/wine_dataset/WinePredictor.csv")


if __name__ == "__main__":
    main()